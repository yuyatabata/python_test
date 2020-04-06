import unittest
from A import solve

class Test_solve(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(3,3),10)

if __name__ == "__main__":
    unittest.main()