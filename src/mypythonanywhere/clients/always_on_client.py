from ..types.requests.always_on_requests import GetAlwaysOns, CreateAlwayOn
from ..pythonanywhere import PythonAnywhereClient


class PythonAnywhereAlwaysOnClient:
    def __init__(self, raw_client: PythonAnywhereClient) -> None:
        self._raw_client = raw_client

    async def get_always_ons(self):
        """ Get a list of all always ons. """
        request = GetAlwaysOns()
        return await self._raw_client(request)

    async def create_always_on(self, command: str, description: str, enabled: bool):
        """ Create a new always on task.

        Args:
            command (str): The command to run.
            description (str): A description of the command.
            enabled (bool): Whether the command is enabled.
        """
        request = CreateAlwayOn(command, description, enabled)
        return await self._raw_client(request)
