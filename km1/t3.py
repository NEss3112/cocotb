import asyncio

import numpy as np
from datetime import datetime
import random as rnd

from collections.abc import Callable
RealFunc = Callable[[float], float]  # type alias for a real -> real function

# def newton(
    # function: RealFunc,
    # derivative: RealFunc,
    # starting_int: int,
# ) -> float:
    # """Newton's Method."""
    # prev_guess = float(starting_int)
    # while True:
        # try:
            # next_guess = prev_guess - function(prev_guess) / derivative(prev_guess)
        # except ZeroDivisionError:
            # raise ZeroDivisionError("Could not find root") from None
        # if abs(prev_guess - next_guess) < 10**-5:
            # return next_guess
        # prev_guess = next_guess

async def newton(
    function: RealFunc,
    derivative: RealFunc,
    starting_int: int,
) -> float:
    """Newton's Method."""
    prev_guess = float(starting_int)
    while True:
        try:
            next_guess = prev_guess - function(prev_guess) / derivative(prev_guess)
        except ZeroDivisionError:
            raise ZeroDivisionError("Could not find root") from None
        if abs(prev_guess - next_guess) < 10**-5:
            return next_guess
        prev_guess = next_guess


delay = [0.5, 0.75, 1, 1.25, 1.5]

async def Task(index):
    pass

async def main():
    pass









