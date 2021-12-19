from .Operators import Operators
from .Calculation import Calculation


class Multiplication(Calculation):
    def __init__(self):
        super().__init__(Operators.MULTIPLICATION)

    def formatCorrectedString(self):
        return (
            f"{self._a} {self._operator.value} {self._b} = "
            f"{self._a * self._b}"
        )
