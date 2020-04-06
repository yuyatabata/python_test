import unittest
from B import solve

class Test_B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(4,9,[3,3,3,3]),4)

if __name__ == "__main__":
    unittest.main()
 