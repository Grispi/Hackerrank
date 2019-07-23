
class Scopetiando:
    def __init__(self):
        self.b = True
        self.x = 88

    def Scope(self):
        self.d = 9.0
        # print(example(9))
        # classVariable()

    def example(self, x):
        print("----- example(x):\n",
              "Initial value of Local Variable `x`: ", x, "\n")
        x = 4.4

        print("New value of Local Variable `x`: ", x, "\n")

        for i in range(4):
            b = i + 4
            print("For Loop 1 in example(double x):\n", "Local Variable `b` (local to loop): ", i, "\n",
                  "Local Variable `i` (local to loop): ", b, "\n",
                  "Local Variable `x` (method parameter): ", x, "\n")

    def classVariable(self):
        print("----- classVariable():\n",
              "Instance Variable `b`: ",  self.b, "\n"
              "Instance Variable `x`: ", self.x)


s = Scopetiando()
s.Scope()
s.example(9)
s.classVariable()
