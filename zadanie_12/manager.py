class Manager:

    def __init__(self):
        self.actions = {}

    def assign(self, name):
        def decorate(func):
            self.actions[name] = func
        return decorate

    def execute(self, name, *args):
        if name not in self.actions:
            print("Action not defined")
        else:
            return self.actions[name](*args)