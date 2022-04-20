import unittest
from pathlib import Path

from src.mypythonanywhere import AccountType, FriendlyPythonAnywhereClient
from mypythonanywhere.types.requests.file import (DeleteFile,
                                                  GetPath,
                                                  GetTree,
                                                  UploadFile)

from helpers import load_account_details_from_env


class FilesTest(unittest.IsolatedAsyncioTestCase):

    def setUp(self) -> None:
        (username, token, account_type) = load_account_details_from_env()

        self.client = FriendlyPythonAnywhereClient(
            username=username,
            token=token,
            account_type=AccountType(account_type)
        )

    async def test_get_tree(self):
        files = await self.client(GetTree('/'))
        self.assertIsNotNone(files)

    async def test_get_files(self):
        files = await self.client(GetPath('home/MerrilleChoate'))
        self.assertIsNotNone(files)

    async def test_get_path_entire_tree(self):
        async with self.client:
            tree = await self.client(GetTree('/'))
            for path in tree:
                if path.startswith('/var/'):
                    continue

                files = await self.client(GetPath(path))
                self.assertIsNotNone(files)

    async def test_upload_file(self):
        await self.client(UploadFile(
            Path(__file__).parent.resolve().joinpath('test_file_to_send.txt'),
            'home/MerrilleChoate/my_file.txt'))

    async def test_upload_and_delete_file(self):
        async with self.client:
            await self.client(UploadFile(
                Path(__file__).parent.resolve().joinpath(
                    'test_file_to_send.txt'),
                'home/MerrilleChoate/my_file.txt'))

            await self.client(DeleteFile('home/MerrilleChoate/my_file.txt'))


if __name__ == '__main__':
    unittest.main()
