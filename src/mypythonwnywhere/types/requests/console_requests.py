from ..base_request import BaseRequest
from ..request_method import RequestMethod
from ..models.console import Console


class GetConsoles(BaseRequest[list[Console]]):
    def __init__(self):
        super().__init__('consoles', RequestMethod.GET)

    def get_return_value(self, data) -> list[Console]:
        return [Console(**console) for console in data]

    def _get_input_parameters(self):
        return {}

    def _get_input_data(self):
        return {}


class CreateConsole(BaseRequest[Console]):
    def __init__(
            self,
            executable: str,
            arguments: list[str] = None,
            working_directory: str = None) -> None:
        super().__init__('consoles', RequestMethod.POST)
        self._executable = executable
        self._arguments = ' '.join(arguments) if isinstance(
            arguments, list) else None
        self._working_directory = working_directory

    def get_return_value(self, data) -> Console:
        return Console(**data)

    def _get_input_parameters(self):
        return {
            'executable': self._executable,
            'arguments': self._arguments,
            'working_directory': self._working_directory
        }

    def _get_input_data(self):
        return {}


class GetSharedConsoles(BaseRequest[list[Console]]):
    def __init__(self):
        super().__init__('consoles/shared_with_you', RequestMethod.GET)

    def get_return_value(self, data) -> list[Console]:
        return [Console(**console) for console in data]

    def _get_input_parameters(self):
        return {}

    def _get_input_data(self):
        return {}


class GetConsoleInfo(BaseRequest[Console]):
    def __init__(self, console_id: int) -> None:
        super().__init__('consoles/{console_id}'.format(console_id=console_id),
                         RequestMethod.GET)

    def get_return_value(self, data) -> Console:
        return Console(**data)

    def _get_input_parameters(self):
        return {}

    def _get_input_data(self):
        return {}


class KillConsole(BaseRequest[None]):
    def __init__(self, console_id: int) -> None:
        super().__init__('consoles/{console_id}'.format(console_id=console_id),
                         RequestMethod.DELETE)

    def get_return_value(self, data):
        return None

    def _get_input_parameters(self):
        return {}

    def _get_input_data(self):
        return {}


class GetConsoleOutput(BaseRequest[str]):
    def __init__(self, console_id: int) -> None:
        super().__init__('consoles/{console_id}/get_latest_output'.format(
            console_id=console_id), RequestMethod.GET)

    def get_return_value(self, data):
        return data["output"]

    def _get_input_parameters(self):
        return {}

    def _get_input_data(self):
        return {}


class SendConsoleInput(BaseRequest[None]):
    def __init__(self, console_id: int, input_text: str) -> None:
        super().__init__('consoles/{console_id}/send_input'.format(
            console_id=console_id), RequestMethod.POST)
        self._input_text = input_text

    def get_return_value(self, data):
        return None

    def _get_input_parameters(self):
        return {}

    def _get_input_data(self):
        return {
            'input': self._input_text
        }
