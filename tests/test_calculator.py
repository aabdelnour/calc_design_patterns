# tests/test_calculator.py

import pytest
from calculator.calculator import Calculator
from calculator.operations import Addition, Subtraction, Multiplication, Division

def test_addition():
    calc = Calculator(Addition())
    assert calc.calculate(1, 2) == 3

def test_subtraction():
    calc = Calculator(Subtraction())
    assert calc.calculate(5, 3) == 2

def test_multiplication():
    calc = Calculator(Multiplication())
    assert calc.calculate(3, 4) == 12

def test_division():
    calc = Calculator(Division())
    assert calc.calculate(10, 2) == 5

def test_division_by_zero():
    calc = Calculator(Division())
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.calculate(10, 0)
