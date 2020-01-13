import sys
import os
import importlib

from .plugin import Plugin


class Loader:
    def __init__(self, path, plugin_cls, stderr=sys.stderr):
        if not os.path.exists(path):
            raise NotADirectoryError("Cant find plugins directory")
        if plugin_cls not in Plugin.__subclasses__():
            raise TypeError("plugin_cls needs to implement plugin.Plugin")
        self.stderr = stderr
        self.path = path
        self.plugin_cls = plugin_cls
        sys.path.append(self.path)
        self.plugins = []

    def load(self, *args, **kwargs):
        files = os.listdir(self.path)
        for fname in files:
            module, ext = os.path.splitext(fname)
            importlib.import_module(module)

        for cls in self.plugin_cls.__subclasses__():
            try:
                plugin = cls(*args, **kwargs)
            except Exception as ex:
                self.stderr.write(f"{ex} caught during instantiate {cls}")
                continue
            try:
                plugin.load()
            except Exception as ex:
                self.stderr.write(f"{ex} caught during loading {plugin}")
                continue
            self.plugins.append(plugin)

    def unload(self, *args, **kwargs):
        for plugin in self.plugins:
            try:
                plugin.unload(*args, **kwargs)
            except Exception as ex:
                self.stderr.write(f"{ex} caught during unloading {plugin}")

    def get(self, name):
        for plugin in self.plugins:
            if plugin.name == name:
                return plugin
        raise AttributeError(f"Cant find Plugin {name}")
