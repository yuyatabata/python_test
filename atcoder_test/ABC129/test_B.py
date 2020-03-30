import unittest
from B import solve

class Test_B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(4,[1,3,1,1]),2)

if __name__ == "__main__":
    unittest.main()
 