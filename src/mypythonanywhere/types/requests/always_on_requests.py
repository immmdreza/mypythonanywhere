from ..base_request import BaseRequest
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

    def get_return_value(self, data: JsonValue):
        return data

    def _get_input_parameters(self) -> JsonObject:
        return {}

    def _get_input_data(self) -> JsonObject:
        return {}


class CreateAlwayOn(BaseRequest[None]):
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

    def get_return_value(self, data: JsonValue):
        return None

    def _get_input_parameters(self):
        return {
            'command': self._command,
            'description': self._description,
            'enabled': self._enabled
        }

    def _get_input_data(self) -> JsonObject:
        return {}
