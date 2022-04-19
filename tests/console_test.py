import unittest

from src.mypythonanywhere import AccountType, FriendlyPythonAnywhereClient

from helpers import load_account_details_from_env


class ConsoleTest(unittest.IsolatedAsyncioTestCase):

    def setUp(self) -> None:
        (username, token, account_type) = load_account_details_from_env()

        self.client = FriendlyPythonAnywhereClient(
            username=username,
            token=token,
            account_type=AccountType(account_type)
        )

    async def test_create_and_kill_console(self):
        async with self.client:
            consoles = await self.client.console.get_consoles()
            for x in consoles:
                await self.client.console.kill_console(x.id)

            console = await self.client.console.create_console("python3.9", [], "")
            await self.client.console.kill_console(console.id)

            consoles = await self.client.console.get_consoles()
            self.assertFalse(any([x for x in consoles if x.id == console.id]))

    async def test_get_consoles(self):
        consoles = await self.client.console.get_consoles()
        self.assertTrue(isinstance(consoles, list))  # type: ignore


if __name__ == '__main__':
    unittest.main()
