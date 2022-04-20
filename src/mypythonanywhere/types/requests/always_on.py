import aiohttp


from ..base_request import BaseRequest, BaseOrder
from ..request_method import RequestMethod
from ..custom_type_alias import JsonObject, JsonValue


class GetAlwaysOns(BaseRequest[JsonValue]):
    """ List all your consoles

    Args:
        `BaseRequest (list)`: The list of always ons.
    """

    def __init__(self):
        """ List all your consoles
        """
        super().__init__('always_on', RequestMethod.GET)

    async def get_return_value(
            self, http_response: aiohttp.ClientResponse):

        data = await self.ensure_getting_json_response(http_response)
        return data

    def _get_input_parameters(self) -> JsonObject:
        return {}

    def _get_input_data(self) -> JsonObject:
        return {}


class CreateAlwayOn(BaseOrder):
    """ Create a new always on task.

    Args:
        `BaseRequest (None)`: Returns None.
    """

    def __init__(self, command: str, description: str, enabled: bool):
        """ Create a new always on task.

        Args:
            `command (str)`: The command to run.
            `description (str)`: A description of the command.
            `enabled (bool)`: Whether the command is enabled.
        """
        super().__init__('always_on', RequestMethod.POST)
        self._command = command
        self._description = description
        self._enabled = enabled

    def _get_input_parameters(self):
        return {
            'command': self._command,
            'description': self._description,
            'enabled': self._enabled
        }

    def _get_input_data(self) -> JsonObject:
        return {}
