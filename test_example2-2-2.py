import unittest
from calc import Calculator

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        print("create Calculator")

    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(5,2),7)

    def test_sub(self):
        calc = Calculator()
        self.assertEqual(calc.sub(5,2),3)

    def test_mul(self):
        calc = Calculator()
        self.assertEqual(calc.mul(5,2),10)

    def test_div(self):
        calc = Calculator()
        self.assertEqual(calc.div(5,2),2)

if __name__=="__main__":
    unittest.main()
