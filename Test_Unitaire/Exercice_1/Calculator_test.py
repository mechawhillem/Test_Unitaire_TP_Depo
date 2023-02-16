import unittest

class Calculator:

    def add(self, x, y):
        return x + y

    def substract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        assert 0 < y
        return x / y
        
    def power(self, x, y):
        result = 1
        for i in range(y):
            result *= x
        return result
    
    def square_root(self, x):
        if x == 0 or x == 1:
            return x
        val = x
        precision = 0.0000001
        while abs(val - x / val) > precision:
            val = (val + x / val) / 2
        return val
    
    def calculate(self, operation, x, y):
        if operation == "add":
            result = Calculator.add(x,y)
        elif operation == "substract":
            result = Calculator.substract(x,y)
        elif operation == "multiply":
            result = Calculator.multiply(x,y)
        elif operation == "divide":
            result = Calculator.divide(x,y)
        elif operation == "power":
            result = Calculator.power(x,y)
        elif operation == "square_root":
            result = Calculator.square_root(x)
        return result
    
        
#operation = input("Enter the operation you would like to perform (add, subtract, multiply, divide, square_root, power): ")
#num1 = int(input("Enter the first number : "))
#num2 = int(input("Enter the second number : "))
#print(Calculator.calculate(operation,num1,num2))

class TestCalculMethods(unittest.TestCase):

    def test_add(self):
        calculator  = Calculator()
        self.assertEqual(calculator.add(5,4), 9)
    
    def test_substract(self):
        calculator  = Calculator()
        self.assertEqual(calculator.substract(5,4), 1)

    def test_divide(self):
        calculator  = Calculator()
        self.assertEqual(calculator.divide(4,4), 1)
    
    def test_multiply(self):
        calculator  = Calculator()
        self.assertEqual(calculator.multiply(10000000000000,10000000000000), 100000000000000000000000000)

    def test_power(self):
        calculator  = Calculator()
        self.assertEqual(calculator.power(5,5), 3125)

    def test_square_root(self):
        calculator  = Calculator()
        self.assertEqual(calculator.square_root(5), 2.236067977499978)



if __name__ == '__main__':
    unittest.main()
