from random import choice
from .Operators import Operators
from .Calculation import Calculation


class Unities(Calculation):
    _unities = {
        1: "unités",
        10: "dizaines",
        100: "centaines",
    }

    def __init__(self):
        super().__init__(Operators.UNITIES)

    def generateValues(self, generator):
        self._a = (generator.new(), choice([x for x in self._unities]))
        self._b = (generator.new(), choice([x for x in self._unities]))

    def formatString(self):
        return (
            f"{self._a[0]} {self._unities[self._a[1]]} et "
            f"{self._b[0]} {self._unities[self._b[1]]}"
        )

    def formatCorrectedString(self):
        result = self._a[0] * self._a[1] + self._b[0] * self._b[1]

        return (
            f"{self._a[0]} {self._unities[self._a[1]]} et "
            f"{self._b[0]} {self._unities[self._b[1]]} = "
            f"{result}"
        )
