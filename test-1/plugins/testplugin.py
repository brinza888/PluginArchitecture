from plugin import MyPlugin


class Test (MyPlugin):
    name = "Test"
    version = "1.0"
    author = "Brinza Bezrukoff"
    description = "Test plugin"

    def load(self):
        self.ev_manager["prog_running"] += self.prog_running_event
        print("Test plugin loaded!")

    def prog_running_event(self, *args, **kwargs):
        print("Event confirmed")

    def unload(self):
        self.ev_manager["prog_running"] -= self.prog_running_event
        print("Test plugin unloaded!")
