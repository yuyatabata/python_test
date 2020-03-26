import unittest
from unittest.mock import MagicMock
from unittest import mock
import mock_snackapi

class TestThirdPartyMotherRequestSnackApi(unittest.TestCase):
    def setUp(self):
        self.patcher = mock.patch('mock_snackapi.ThirdPartyMotherRequestSnackApi.request_snack')
        self.mock_snack = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()
        
    def test_request_snack_patch_patcher(self):
        self.mock_snack.return_value = 'せんべい'

        result = mock_snackapi.ChildGetSnackApi(name='test', hungry='満腹', time=15)
        snack_name = result.get_snack()

        self.assertEqual(snack_name, 'せんべい')
        self.mock_snack.assert_called()

#返答
if __name__ == "__main__":
    unittest.main()