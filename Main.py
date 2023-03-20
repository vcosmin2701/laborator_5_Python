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


class Calculator2(Calculator):
    def __init__(self, nr):
        super().__init__(nr)

    def negative(self):
        self.nr = -self.nr


c = Calculator(4)
c.multiplication(3)
c.division(2)
c.output_result()
c1 = Calculator2(2)
c1.negative()
c1.multiplication(2)
c1.output_result()
