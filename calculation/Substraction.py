from .Operators import Operators
from .Calculation import Calculation


class Substraction(Calculation):
    def __init__(self):
        super().__init__(Operators.SUBSTRACTION)

    def isValid(self):
        return (self._a - self._b) > 0

    def generateValues(self, generator):
        self._a = generator.newFromLevel()
        self._b = generator.newFromLevel()

        valid = self.isValid()
        while valid is False:
            self._a = generator.newFromLevel()
            self._b = generator.newFromLevel()
            valid = self.isValid()
