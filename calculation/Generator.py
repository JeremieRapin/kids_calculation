from .Operators import Operators
from .LevelName import LevelName
from random import choice, randrange


class Generator:
    _level = None
    _operators = list()

    LEVEL_EASY_HIGHEST = 10
    LEVEL_MEDIUM_HIGHEST = 20
    LEVEL_PRO_ADVANCED_NOMINAL = 100
    DIVIDER_MAX = 10
    DIVIDEND_MAX = 100

    _levels = {
        LevelName.EASY: 0,
        LevelName.MEDIUM: 1,
        LevelName.PRO: 2,
        LevelName.ADVANCED: 3,
    }

    def __init__(self, level):
        self._level = [x for x in LevelName if x.value == level][0]
        self.initOperators(level)

    def getHighest(self):
        if self._levels[self._level] >= self._levels[LevelName.PRO]:
            return self.LEVEL_PRO_ADVANCED_NOMINAL
        elif self._levels[self._level] == self._levels[LevelName.MEDIUM]:
            return self.LEVEL_MEDIUM_HIGHEST
        else:
            return self.LEVEL_EASY_HIGHEST

    def initOperators(self, level):
        self._operators = list()
        self._operators.append(Operators.ADDITION)
        self._operators.append(Operators.SUBSTRACTION)

        if self._levels[self._level] >= self._levels[LevelName.PRO]:
            self._operators.append(Operators.MULTIPLICATION)
            self._operators.append(Operators.UNITIES)

        if self._levels[self._level] >= self._levels[LevelName.ADVANCED]:
            self._operators.append(Operators.DIVISION)
            self._operators.append(Operators.MULTIPLE)
            self._operators.append(Operators.FRACTION)

    def newOperator(self):
        return choice(self._operators)

    def new(self, start=0, stop=None):
        return randrange(start=start, stop=stop or self.LEVEL_EASY_HIGHEST)

    def newFromLevel(self):
        return randrange(self.getHighest())

    def newDividend(self):
        return self.new(start=1, stop=self.DIVIDEND_MAX)

    def newDivider(self):
        return self.new(start=2, stop=self.DIVIDER_MAX)
