
from typing import Iterable

def add(a: float, b: float) -> float:
    return a + b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("b must not be zero")
    return a / b

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def clamp(x: float, low: float, high: float) -> float:
    assert low <= high, "low should not exceed high"
    return max(low, min(high, x))

def mean(xs: Iterable[float]) -> float:
    xs = list(xs)
    if not xs:
        raise ValueError("xs must be non-empty")
    return sum(xs) / len(xs)
