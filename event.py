class Event:
    def __init__(self):
        self.subscribes = []

    def subscribe(self, func):
        self.subscribes.append(func)

    def cancel(self, func):
        self.subscribes.remove(func)

    def __iadd__(self, other):
        self.subscribe(other)

    def __isub__(self, other):
        self.cancel(other)

    def run(self, *args, **kwargs):
        for sub in self.subscribes:
            sub(*args, **kwargs)
