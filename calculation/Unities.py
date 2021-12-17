from random import choice
from .Operators import Operators
from .Calculation import Calculation


class Unities(Calculation):
    _unities = (
        "dizaines",
        "centaines",
        "unités",
    )

    def __init__(self):
        super().__init__(Operators.UNITIES)

    def generateValues(self, generator):
        self._a = generator.new()
        self._b = generator.new()

    def formatString(self):
        return (
            f"{self._a} {choice(self._unities)} et "
            f"{self._b} {choice(self._unities)}"
        )
