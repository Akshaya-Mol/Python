class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    
    def sub(self):
        return self.num1 - self.num2
    
    def mul(self):
        return self.num1 * self.num2
    
    def div(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error! Division by zero."

calc = Calculator(5, 8)

print("Addition:", calc.add())
print("Subtraction:", calc.sub())
print("Multiplication:", calc.mul())
print("Division:", calc.div())
