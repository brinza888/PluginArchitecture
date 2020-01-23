from abc import ABCMeta, abstractmethod


class Plugin (metaclass=ABCMeta):
    def __init__(self, ev_manager, *args, **kwargs):
        self.ev_manager = ev_manager

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def version(self):
        pass

    @property
    def author(self):
        return "*undefined*"

    @property
    def description(self):
        return "*undefined*"

    def load(self):
        pass

    def unload(self):
        pass

    def __repr__(self):
        return f"Plugin({self.name}-{self.version})"
