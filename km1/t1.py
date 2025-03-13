from time import time, asctime

# Newton's Method - https://en.wikipedia.org/wiki/Newton%27s_method
from collections.abc import Callable

def timer_arg(timer_mode = "simple"):
    def timer(func):
        def wrapper(*args):
            
            if timer_mode == "full": 
                flag = True
            elif timer_mode == "simple": 
                flag = False
            else:
                raise Exception("Modes can only be either \"simple\" or \"full\"")
            
            print(f"calling function {func.__name__}")
            if flag: print(f"start_time = {asctime()}")
            start_time = time()
            res = func(*args)
            end_time = time()
            if flag: print(f"finish_time = {asctime()}")
            print(f"Execution time = {(end_time - start_time)*1e6:.2f} us")
            return res
        return wrapper
    return timer

RealFunc = Callable[[float], float]  # type alias for a real -> real function


# function is the f(x) and derivative is the f'(x)
@timer_arg(timer_mode="full")
def newton(
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

def main() -> None:
    newton(lambda x: x**10, lambda x: 10*x**9, 1)

if __name__ == "__main__":
    main()