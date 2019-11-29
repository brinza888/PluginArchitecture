from abc import ABCMeta


class Plugin (metaclass=ABCMeta):
    def __init__(self):
        pass

    def load(self):
        pass

    def unload(self):
        pass
