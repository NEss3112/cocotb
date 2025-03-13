from t1 import newton
from numpy import log, exp

def test(margin, func, der, start_int):
    res = newton(func, der, start_int)
    print(res)
    print(f"{func(res) = }")
    assert func(res) > -margin and func(res) < margin, "Result does not meet margins"

def main():
    print("=====================TESTING=====================")
    test(1e-10, lambda x: x**2, lambda x: 2*x, 10)
    print("=================================================")
    test(1e-10, lambda x: x**3, lambda x: 3*x**2, 10)
    print("=================================================")
    test(1e-10, lambda x: 2*x**2 - 5*x - 5, lambda x: 4*x - 5, 10)
    print("=================================================")

    test(1e-15, lambda x: x**2, lambda x: 2*x, 10)
    print("=================================================")
    test(1e-15, lambda x: x**3, lambda x: 3*x**2, 10)
    print("=================================================")
    test(1e-15, lambda x: 2*x**2 - 5*x - 5, lambda x: 4*x - 5, 10)
    print("=================================================")


if __name__ == "__main__":
    main()

