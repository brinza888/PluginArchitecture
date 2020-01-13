from pluginarch.loader import Loader
from plugin import MyPlugin


ld = Loader("plugins", MyPlugin)
ld.load()


print("Main part works!")


ld.unload()
