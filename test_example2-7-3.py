#Calculatorクラスを擬似的に操作
import unittest
from calclib import CalculatorLibrary
from calc import Calculator
from mock import patch

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calclib = CalculatorLibrary()
        print("create calculator library")

    @patch.object(Calculator,"add")
    def test_add(self,mock_add):
        mock_add.return_value = 7
        self.assertEqual(self.calclib.calculate(5,2,'+'),7)

    @patch.object(Calculator,"sub")
    def test_sub(self,mock_sub):
        mock_sub.return_value = 3
        self.assertEqual(self.calclib.calculate(5,2,'-'),3)

    @patch.object(Calculator,"mul")
    def test_mul(self,mock_mul):
        mock_mul.return_value = 10
        self.assertEqual(self.calclib.calculate(5,2,'*'),10)

    @patch.object(Calculator,"div")
    def test_div(self,mock_div):
        mock_div.return_value = 2
        self.assertEqual(self.calclib.calculate(5,2,'/'),2)

    def test_exception(self):
        with self.assertRaises(ValueError):
            self.calclib.calculate(5,2,'?')


if __name__=="__main__":
    unittest.main()
