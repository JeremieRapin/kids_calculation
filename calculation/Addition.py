from .Operators import Operators
from .Calculation import Calculation


class Addition(Calculation):
    def __init__(self):
        super().__init__(Operators.ADDITION)

    def isValid(self):
        return (self._a + self._b) <= 100

    def generateValues(self, generator):
        self._a = generator.newFromLevel()
        self._b = generator.newFromLevel()

        valid = self.isValid()
        while valid is False:
            self._a = generator.newFromLevel()
            self._b = generator.newFromLevel()
            valid = self.isValid()

    def formatCorrectedString(self):
        return (
            f"{self._a} {self._operator.value} {self._b} = "
            f"{self._a + self._b}"
        )
