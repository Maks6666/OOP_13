class Calculator:
    def add(self, x, y):
        return x + y
    def subtract(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            raise ZeroDivisionError("Zero division error")
    def __call__(self, action, x, y):
        if action == "add":
            return self.add(x, y)
        elif action == "subtract":
            return self.subtract(x, y)
        elif action == "multiply":
            return self.multiply(x, y)
        elif action == "divide":
            return self.divide(x, y)
        else:
            print("Wrong action.")

calculator = Calculator()
print(calculator("add", 2, 4))









