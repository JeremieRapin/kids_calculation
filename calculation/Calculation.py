from .Operators import Operators


class Calculation:
    _a = None
    _b = None
    _operator = Operators

    def __init__(self, operator):
        self._operator = operator

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @a.setter
    def a(self, a):
        self._a = a

    @b.setter
    def b(self, b):
        self._b = b

    def isValid(self):
        return True

    def formatString(self):
        return f"{self._a} {self._operator.value} {self._b}"

    def formatCorrectedString(self):
        raise Exception("formatCorrectedString must be overloaded")

    def generateValues(self, generator):
        self._a = generator.new()
        self._b = generator.new()
