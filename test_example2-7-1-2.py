import unittest
from calc import Calculator
from mock import patch

class MyTestCase(unittest.TestCase):
    def test_add_normal(self):
        calc = Calculator()
        self.assertEqual(calc.add(1,2),3)

    @patch.object(Calculator,"sub")
    def test_add_mock_return_100(self,mock_sub):
        mock_sub.return_value = 100
        calc = Calculator()
        self.assertEqual(calc.sub(1,2),100)

    @patch.object(Calculator,"mul")
    def test_add_mock_return_200(self,mock_mul):
        mock_mul.return_value = 200
        calc = Calculator()
        self.assertEqual(calc.add(1,2),200)

if __name__=="__main__":
    unittest.main()
