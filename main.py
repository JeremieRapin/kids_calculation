#!/bin/python3

import argparse
from calculation.Engine import Engine
from calculation.LevelName import LevelName

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate some calculations for kids",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--numbers",
        type=int,
        help="number of calculations to generate",
        default=100,
    )
    parser.add_argument(
        "--level",
        choices=[x.value for x in LevelName],
        default=LevelName.ADVANCED.value,
        help="level of calculations",
    )
    parser.add_argument(
        "--column",
        type=int,
        default=Engine.COLUMN_NUMBERS,
        help="the number of column to display",
    )

    args = parser.parse_args()
    engine = Engine(args.numbers, args.level, args.column)
    engine.generate()
    engine.display()
