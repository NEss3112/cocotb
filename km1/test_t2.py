from t1 import newton

def test_newton():
    margin = 1e-7
    expected_root = 0
    res = newton(lambda x: x**2, lambda x: 2*x, 1)
    print(f"{res = }")
    assert res > (expected_root - margin) and (expected_root - margin)

def test_newton1():
    margin = 1e-7
    expected_root = 0
    res = newton(lambda x: x**3, lambda x: 3*x**2, 1)
    print(f"{res = }")
    assert res > (expected_root - margin) and (expected_root - margin)

def test_newton2():
    margin = 1e-7
    expected_root = 1
    res = newton(lambda x: x**2 - 1, lambda x: 2*x, 1)
    print(f"{res = }")
    assert res > (expected_root - margin) and (expected_root - margin)

def test_newton3():
    margin = 1e-7
    expected_root = 0
    res = newton(lambda x: 2*x**2, lambda x: 4*x, 1)
    print(f"{res = }")
    assert res > (expected_root - margin) and (expected_root - margin)

def test_newton4():
    margin = 1e-7
    expected_root = -3
    res = newton(lambda x: x + 3, lambda x: 1, 1)
    print(f"{res = }")
    assert res > (expected_root - margin) and (expected_root - margin)