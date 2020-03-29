try:
    from unittest import mock
except ImportError:
    import mock

import unittest
import sample

class Test_Sample(unittest.TestCase):
    def test_add(self):
        obj = sample.Sample()
        obj._take_a_long_time = mock.Mock()
        result = obj.do_something()
        self.assertEqual(result, 'Hello, World!')
        obj._take_a_long_time.asset_called_once_with()

if __name__=="__main__":
    unittest.main()