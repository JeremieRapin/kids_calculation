from random import choice
from .Division import Division


class Fraction(Division):
    _fractions = {
        2: "demi",
        3: "tiers",
        4: "quart",
        5: "cinquième",
        6: "sixième",
    }

    def __init__(self):
        super().__init__()

    def formatString(self):
        return f"le {self._fractions[self._b]} de {self._a}"

    def generateValues(self, generator):
        division = Division()
        self._b = choice([x for x in self._fractions])
        division.generateValues(generator, self._b)
        self._a = division.a

    def formatCorrectedString(self):
        return (
            f"le {self._fractions[self._b]} de {self._a} = "
            f"{int(self._a / self._b)}"
        )
