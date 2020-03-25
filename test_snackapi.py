import unittest
from unittest.mock import MagicMock
import mock_snackapi

class TestThirdPartyMotherRequestSnackApi(unittest.TestCase):
    def test_request_snack(self):
        result = mock_snackapi.ChildGetSnackApi(name='test', hungry='満腹')
        result.mother_request_api.request_snack = MagicMock(return_value='せんべい')

        self.assertEqual(result.get_snack(), 'せんべい')

#返答
if __name__ == "__main__":
    unittest.main()