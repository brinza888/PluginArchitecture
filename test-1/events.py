from pluginarch.event import Event
from pluginarch.event import EventManager


events = [
    Event("prog_running")
]

EvManager = EventManager()
EvManager.extend(events)
