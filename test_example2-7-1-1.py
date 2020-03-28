import unittest
from calc import Calculator
from mock import patch

class MyTestCase(unittest.TestCase):
    def test_add_normal(self):
        calc = Calculator()
        self.assertEqual(calc.add(1,2),3)

    #patchを書くことで上書きできる
    #Calculatorのaddメソッドをmockから操作
    @patch.object(Calculator,"add")
    def test_add_mock_return_100(self,mock_add):
        mock_add.return_value = 100
        calc = Calculator()
        self.assertEqual(calc.add(1,2),100)

    @patch.object(Calculator,"add")
    def test_add_mock_return_200(self,mock_add):
        mock_add.return_value = 200
        calc = Calculator()
        self.assertEqual(calc.add(1,2),200)

if __name__=="__main__":
    unittest.main()
