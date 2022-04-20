from ..types.requests.console import (CreateConsole, GetConsoleInfo,
                                               GetConsoleOutput, GetConsoles,
                                               GetSharedConsoles, KillConsole,
                                               SendConsoleInput)
from ..pythonanywhere import PythonAnywhereClient


class PythonAnywhereConsoleClient:
    def __init__(self, raw_client: PythonAnywhereClient) -> None:
        self._raw_client = raw_client

    async def get_consoles(self):
        """ Get a list of all consoles. """
        request = GetConsoles()
        return await self._raw_client(request)

    async def create_console(
            self, executable: str, arguments: list[str], working_directory: str):
        """ Create a console.

        Args:
            executable (str): The executable to run.
            arguments (list[str]): The arguments to pass to the executable.
            working_directory (str): The working directory to run the executable in.
        """
        request = CreateConsole(executable, arguments, working_directory)
        return await self._raw_client(request)

    async def get_shared_consoles(self):
        """ Get a list of all shared consoles. """
        request = GetSharedConsoles()
        return await self._raw_client(request)

    async def get_console_info(self, console_id: int):
        """ Get information about a console.

        Args:
            console_id (int): The id of the console.
        """
        request = GetConsoleInfo(console_id)
        return await self._raw_client(request)

    async def kill_console(self, console_id: int):
        """ Kill a console.

        Args:
            console_id (int): The id of the console.
        """
        request = KillConsole(console_id)
        return await self._raw_client(request)

    async def get_console_output(self, console_id: int):
        """ Get the output of a console.

        Args:
            console_id (int): The id of the console.
        """
        request = GetConsoleOutput(console_id)
        return await self._raw_client(request)

    async def send_console_input(self, console_id: int, input_text: str):
        """ Send input to a console.

        Args:
            console_id (int): The id of the console.
            input_text (str): The text to send to the console.
        """
        request = SendConsoleInput(console_id, input_text)
        return await self._raw_client(request)
