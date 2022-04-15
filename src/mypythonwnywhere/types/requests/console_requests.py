from ..base_request import BaseRequest
from ..request_method import RequestMethod
from ..models.console import Console


class GetConsoles(BaseRequest[list[Console]]):
    def __init__(self):
        super().__init__('consoles', RequestMethod.GET)

    def get_return_value(self, data) -> list[Console]:
        return [Console(**console) for console in data]

    def get_input_parameters(self):
        return {}


class CreateConsole(BaseRequest[None]):
    def __init__(
            self, executable: str, arguments: list[str], working_directory: str) -> None:
        super().__init__('consoles', RequestMethod.POST)
        self._executable = executable
        self._arguments = ' '.join(arguments)
        self._working_directory = working_directory

    def get_return_value(self, data) -> None:
        return None

    def get_input_parameters(self):
        return {
            'executable': self._executable,
            'arguments': self._arguments,
            'working_directory': self._working_directory
        }
