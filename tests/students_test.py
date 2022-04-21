import logging
import sys
import unittest

from src.mypythonanywhere import AccountType, FriendlyPythonAnywhereClient
from src.mypythonanywhere.types.requests.students import (GetStudents)

from helpers import load_account_details_from_env

logging.basicConfig(level=logging.INFO, handlers=[
    logging.StreamHandler(sys.stdout)
])


class StudentsTest(unittest.IsolatedAsyncioTestCase):

    def setUp(self) -> None:
        (username, token, account_type) = load_account_details_from_env()

        self.client = FriendlyPythonAnywhereClient(
            username=username,
            token=token,
            account_type=AccountType(account_type)
        )

    async def test_get_students(self):
        students = await self.client(GetStudents())

        self.assertIsInstance(students, list)


if __name__ == '__main__':
    unittest.main()
