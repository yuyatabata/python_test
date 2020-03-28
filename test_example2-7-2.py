import unittest
from calclib import CalculatorLibrary

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calclib = CalculatorLibrary()
        print("create calculator library")

    def test_add(self):
        self.assertEqual(self.calclib.calculate(5,2,'+'),7)

    def test_sub(self):
        self.assertEqual(self.calclib.calculate(5,2,'-'),3)

    def test_mul(self):
        self.assertEqual(self.calclib.calculate(5,2,'*'),10)

    def test_div(self):
        self.assertEqual(self.calclib.calculate(5,2,'/'),2)

    def test_exception(self):
        with self.assertRaises(ValueError):
            self.calclib.calculate(5,2,'?')


if __name__=="__main__":
    unittest.main()
