try:
    from unittest import mock
except ImportError:
    import mock

import unittest
import sample

class Test_Sample(unittest.TestCase):
    @mock.patch('time.sleep')#time.sleepを置き換え
    def test_do_something(self, _mock_sleep):
        obj = sample.Sample()
        result = obj.do_something()
        self.assertEqual(result, 'Hello, World!')

if __name__=="__main__":
    unittest.main()