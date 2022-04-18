import unittest

from src.mypythonanywhere import AccountType, FriendlyPythonAnywhereClient

from helpers import load_account_details_from_env


class ConsoleTest(unittest.TestCase):

    def setUp(self) -> None:
        (username, token, account_type) = load_account_details_from_env()

        self.client = FriendlyPythonAnywhereClient(
            username=username,
            token=token,
            account_type=AccountType(account_type)
        )

    def test_create_and_kill_console(self):
        console = self.client.console.create_console("python3.9", [], "")
        self.client.console.kill_console(console.id)

        consoles = self.client.console.get_consoles()
        self.assertFalse(any([x for x in consoles if x.id == console.id]))


if __name__ == '__main__':
    unittest.main()
