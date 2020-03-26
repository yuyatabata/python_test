import unittest
from unittest.mock import MagicMock
from unittest import mock
import mock_snackapi

class TestThirdPartyMotherRequestSnackApi(unittest.TestCase):

    @mock.patch('mock_snackapi.ThirdPartyMotherRequestSnackApi.request_snack',return_value='せんべい')
    def test_request_snack_path(self, mock_snack):
        result = mock_snackapi.ChildGetSnackApi(name='test', hungry='満腹', time=15)

        self.assertEqual(result.get_snack(), 'せんべい')

        mock_snack.assert_called()

    def test_request_snack_path_with(self):
        with mock.patch(
            'mock_snackapi.ThirdPartyMotherRequestSnackApi.request_snack') as mock_snack:
            mock_snack.return_value = 'せんべい'
            result = mock_snackapi.ChildGetSnackApi(
                name='test', hungry='満腹', time=15)
            snack_name = result.get_snack()

            self.assertEqual(snack_name, 'せんべい')
            mock_snack.asser_called()
        

#返答
if __name__ == "__main__":
    unittest.main()