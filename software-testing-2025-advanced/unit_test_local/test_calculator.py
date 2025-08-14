
import math
import pytest
from app.calculator import add, divide, factorial, clamp, mean

@pytest.mark.parametrize('a,b,expected', [
    (1, 2, 3),
    (-5, 5, 0),
    (1.5, 2.25, 3.75),
])
def test_add(a, b, expected):
    assert add(a, b) == pytest.approx(expected)

def test_divide_basic():
    assert divide(10, 4) == pytest.approx(2.5)

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

@pytest.mark.parametrize('n,expected', [
    (0, 1),
    (1, 1),
    (5, 120),
])
def test_factorial(n, expected):
    assert factorial(n) == expected

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)

@pytest.mark.parametrize('x,low,high,expected', [
    (5, 0, 10, 5),
    (-1, 0, 10, 0),
    (11, 0, 10, 10),
])
def test_clamp(x, low, high, expected):
    assert clamp(x, low, high) == expected

def test_mean_regular():
    assert mean([1, 2, 3, 4]) == 2.5

def test_mean_empty():
    with pytest.raises(ValueError):
        mean([])
