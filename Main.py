class Calculator:
    nr = 0

    def __init__(self, nr):
        self.nr = nr

    def multiplication(self, other):
        self.nr *= other

    def division(self, other):
        self.nr /= other

    def output_result(self):
        print(self.nr)


c = Calculator(4)
c.multiplication(3)
c.division(2)
c.output_result()
