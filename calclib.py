from calc import Calculator

class CalculatorLibrary(object):
    def __init__(self):
        self.calc = Calculator()

    def calculate(self,input_a,input_b,operation):
        if operation == "+":
            return self.calc.add(input_a,input_b)
        elif operation == "-":
            return self.calc.sub(input_a,input_b)
        elif operation == "*":
            return self.calc.mul(input_a,input_b)
        elif operation == "/":
            return self.calc.div(input_a,input_b)
        else:
            raise ValueError("wrong operation")