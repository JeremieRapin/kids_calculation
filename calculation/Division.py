from .Operators import Operators
from .Calculation import Calculation


class Division(Calculation):
    def __init__(self):
        super().__init__(Operators.DIVISION)

    def isValid(self):
        if (
            (self._a / self._b).is_integer()
            and self._a != self._b
            and self._a < self._b * 10
        ):
            return True

        return False

    def generateValues(self, generator, b=None):
        self._a = generator.newDividend()
        if b:
            self._b = b
        else:
            self._b = generator.newDivider()

        valid = self.isValid()
        while valid is False:
            self._a = generator.newDividend()
            if not self._b:
                self._b = generator.newDivider()
            valid = self.isValid()

    def formatCorrectedString(self):
        return (
            f"{self._a} {self._operator.value} {self._b} = "
            f"{int(self._a / self._b)}"
        )
