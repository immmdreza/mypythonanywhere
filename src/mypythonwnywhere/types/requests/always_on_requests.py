from ..base_request import BaseRequest
from ..request_method import RequestMethod


class GetAlwaysOns(BaseRequest[list]):
    def __init__(self):
        super().__init__('always_on', RequestMethod.GET)

    def get_return_value(self, data) -> list:
        return data

    def get_input_parameters(self):
        return {}


class CreateAlwayOn(BaseRequest[None]):
    def __init__(self, command: str, description: str, enabled: bool):
        super().__init__('always_on', RequestMethod.POST)
        self._command = command
        self._description = description
        self._enabled = enabled

    def get_return_value(self, data) -> None:
        return None

    def get_input_parameters(self):
        return {
            'command': self._command,
            'description': self._description,
            'enabled': self._enabled
        }
