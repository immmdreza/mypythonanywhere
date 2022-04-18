import unittest
# import pathlib

from src.mypythonanywhere import AccountType, FriendlyPythonAnywhereClient
# from src.mypythonanywhere.types.requests.file_requests import UploadFile

from helpers import load_account_details_from_env


class FilesTest(unittest.TestCase):

    def setUp(self) -> None:
        (username, token, account_type) = load_account_details_from_env()

        self.client = FriendlyPythonAnywhereClient(
            username=username,
            token=token,
            account_type=AccountType(account_type)
        )

    # def test_upload_file(self):
    #     upload_path = 'tests/test_file.txt'
    #     file_path = pathlib.Path(__file__).parent.resolve().joinpath(
    #         'test_file_to_send.txt')

    #     upload_file = self.client(UploadFile(file_path, upload_path))

    #     self.assertEqual(upload_file, {})


if __name__ == '__main__':
    unittest.main()
