#!/bin/python3

from calculation.Operators import Operators
from calculation.Addition import Addition
from calculation.Substraction import Substraction
from calculation.Multiplication import Multiplication
from calculation.Division import Division
from calculation.Multiple import Multiple
from calculation.Fraction import Fraction
from calculation.Generator import Generator
from calculation.Unities import Unities

LINE_LENGTH_MAX = 35


class Engine:
    COLUMN_NUMBERS = 3

    def __init__(self, numbers, level, columns=COLUMN_NUMBERS):
        self._numbers = numbers
        self._columns = columns
        self._calculations = set()
        self._operations = {
            Operators.ADDITION: Addition,
            Operators.DIVISION: Division,
            Operators.FRACTION: Fraction,
            Operators.MULTIPLE: Multiple,
            Operators.MULTIPLICATION: Multiplication,
            Operators.SUBSTRACTION: Substraction,
            Operators.UNITIES: Unities,
        }
        self._generator = Generator(level)

    def display(self):
        str = ""
        for idx, calculation in enumerate(self._calculations):
            str += f"{calculation.formatString() + ' =' :<{LINE_LENGTH_MAX}}"
            if idx % self._columns == (self._columns - 1):
                print(str)
                str = ""

        if str != "":
            print(str)

    def generate(self):
        self._calculations.clear()
        while len(self._calculations) != self._numbers:
            operator = self._generator.newOperator()
            calculation = self._operations[operator]()
            calculation.generateValues(self._generator)
            self._calculations.add(calculation)
