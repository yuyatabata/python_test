import unittest
from B import solve

class Test_B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(30,-50),-1044)

if __name__ == "__main__":
    unittest.main()
 