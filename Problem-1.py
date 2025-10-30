# Problem-1: Calculator using class
# Author: Mahadevaswamy HS

class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "subtract":
            return self.a - self.b
        elif self.operation == "multiply":
            return self.a * self.b
        elif self.operation == "divide":
            return "Error: Division by zero" if self.b == 0 else self.a / self.b
        else:
            return "Invalid operation"


if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (add/subtract/multiply/divide): ")
    print("Result:", Calculator(a, b, op).calculate())
