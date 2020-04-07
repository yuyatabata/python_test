import unittest
from A import solve

class Test_solve(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve('8080'),'Good')

if __name__ == "__main__":
    unittest.main()