class Calculator:
    def __init__(self, a, b, op):
        self.a = a
        self.b = b
        self.op = op

    def perform_operation(self):
        match self.op:
            case '+':
                print("Addition:", self.a + self.b)
            case '-':
                print("Subtraction:", self.a - self.b)
            case '*':
                print("Multiplication:", self.a * self.b)
            case '/':
                try:
                    print("Division:", self.a / self.b)
                except ZeroDivisionError:
                    print("Error: Division by zero is not allowed.")
            case _:
                print("You have entered an invalid operation. Please cross-check.")


if __name__=='__main__':
    try:
        a = float(input("Enter value a: "))
        b = float(input("Enter value b: "))
        op = input("Enter the operation to be done ['+','-','*','/']: ")

        calc = Calculator(a, b, op)
        calc.perform_operation()

    except ValueError:
        print("Please enter valid numeric values for a and b.")
