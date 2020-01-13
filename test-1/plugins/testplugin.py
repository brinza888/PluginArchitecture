from plugin import MyPlugin


class Test (MyPlugin):
    name = "Test"
    version = "1.0"
    author = "Brinza Bezrukoff"
    description = "Test plugin"

    def load(self):
        print("Test plugin loaded!")

    def unload(self):
        print("Test plugin unloaded!")
