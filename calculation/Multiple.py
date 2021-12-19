from random import choice
from .Operators import Operators
from .Calculation import Calculation


class Multiple(Calculation):
    _multiples = {
        2: "double",
        3: "triple",
        4: "quadruple",
    }

    def __init__(self):
        super().__init__(Operators.MULTIPLE)

    def generateValues(self, generator):
        self._b = generator.new()
        self._a = choice([x for x in self._multiples])
        self._choice = self._multiples[self._a]

    def formatString(self):
        return f"le {self._choice} de {self._b}"

    def formatCorrectedString(self):
        return f"le {self._choice} de {self._b} = " f"{self._a * self._b}"
