# calculator/calculator.py

from .operations import Operation, Addition, Subtraction, Multiplication, Division

class Calculator:
    def __init__(self, operation: Operation):
        self.operation = operation

    def calculate(self, a, b):
        return self.operation.execute(a, b)
