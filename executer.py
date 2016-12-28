class Executer:

    def __init__(self):
        self.executedCommands = []
        self.preFunctions = []
        self.postFunctions = []

    def register_pre_function(self, f):
        self.preFunctions.append(f)

    def register_post_function(self, f):
        self.postFunctions.append(f)

    def execute(self, f):
        for preFunction in self.preFunctions:
            preFunction(f)

        f();
        for postFunction in self.postFunctions:
            postFunction(f)
