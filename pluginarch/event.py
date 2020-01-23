class Event:
    def __init__(self, name):
        self.name = name
        self.subscribes = []

    def subscribe(self, func):
        self.subscribes.append(func)

    def cancel(self, func):
        self.subscribes.remove(func)

    def __iadd__(self, other):
        self.subscribe(other)
        return self

    def __isub__(self, other):
        self.cancel(other)
        return self

    def run(self, *args, **kwargs):
        for sub in self.subscribes:
            sub(*args, **kwargs)

    def __repr__(self):
        return f"Event({self.name})"


class EventManager:
    def __init__(self):
        self.events = []

    def __len__(self):
        return len(self.events)

    def __getitem__(self, item):
        for v in self.events:
            if v.name == item:
                return v
        raise KeyError(f"Cant find Event {item}")

    def __setitem__(self, key, event):
        if not isinstance(event, Event):
            raise TypeError("event must be an instance of Event")
        self.events.remove(self[key])
        self.add(event)

    def add(self, event):
        if not isinstance(event, Event):
            raise TypeError("event must be an instance of Event")
        self.events.append(event)

    def extend(self, events):
        for v in events:
            self.add(v)
