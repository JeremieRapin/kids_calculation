from random import choice
from .Operators import Operators
from .Calculation import Calculation


class Multiple(Calculation):
    _multiples = (
        "double",
        "triple",
        "quadruple",
    )

    def __init__(self):
        super().__init__(Operators.MULTIPLE)

    def generateValues(self, generator):
        self._b = generator.new()
        self._choice = choice(self._multiples)

    def formatString(self):
        return f"le {self._choice} de {self._b}"
