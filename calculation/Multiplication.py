from .Operators import Operators
from .Calculation import Calculation


class Multiplication(Calculation):
    def __init__(self):
        super().__init__(Operators.MULTIPLICATION)
