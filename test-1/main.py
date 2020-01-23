from pluginarch.loader import Loader

from events import EvManager
from plugin import MyPlugin


print("RUN")

ld = Loader("plugins", MyPlugin)
ld.load(ev_manager=EvManager)


print("Main part works!")
EvManager["prog_running"].run()


ld.unload()

print("END")
