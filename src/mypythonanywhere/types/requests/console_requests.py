from typing import Optional

from ..base_request import BaseRequest
from ..custom_type_alias import JsonObject, JsonValue
from ..models.console import Console
from ..request_method import RequestMethod


class GetConsoles(BaseRequest[list[Console]]):
    """ List all your consoles

    Args:
        `BaseRequest (list[Console])`: The list of consoles.
    """

    def __init__(self):
        """ List all your consoles
        """
        super().__init__('consoles', RequestMethod.GET)

    def get_return_value(self, data: JsonValue) -> list[Console]:
        return [
            Console(**console) for console in data if isinstance(console, dict)
        ]

    def _get_input_parameters(self) -> JsonObject:
        return {}

    def _get_input_data(self) -> JsonObject:
        return {}


class CreateConsole(BaseRequest[Console]):
    """
    Create a new console object (NB does not actually start the process.
    Only connecting to the console in a browser will do that).

    Args:
        `BaseRequest (Console)`: The console object.
    """

    def __init__(
            self,
            executable: str,
            arguments: Optional[list[str]] = None,
            working_directory: Optional[str] = None) -> None:
        """ Create a new console object (NB does not actually start the process.
        Only connecting to the console in a browser will do that).

        Args:
            `executable (str)`: The executable to run.
            `arguments (list[str], optional)`: The arguments to pass to the executable. Defaults to None.
            `working_directory (str, optional)`: The working directory to run the executable in. Defaults to None.
        """
        super().__init__('consoles', RequestMethod.POST)
        self._executable = executable
        self._arguments = ' '.join(arguments) if isinstance(
            arguments, list) else None
        self._working_directory = working_directory

    def get_return_value(self, data: JsonValue) -> Console:
        if isinstance(data, dict):
            return Console(**data)
        raise ValueError(
            'Expected a dict, got {} instead.'.format(type(data)))

    def _get_input_parameters(self):
        return {
            'executable': self._executable,
            'arguments': self._arguments,
            'working_directory': self._working_directory
        }

    def _get_input_data(self) -> JsonObject:
        return {}


class GetSharedConsoles(BaseRequest[list[Console]]):
    """ View shared consoles with you.

    Args:
        `BaseRequest (list[Console])`: The list of consoles.
    """

    def __init__(self):
        """ View shared consoles with you.
        """
        super().__init__('consoles/shared_with_you', RequestMethod.GET)

    def get_return_value(self, data: JsonValue) -> list[Console]:
        return [
            Console(**console) for console in data if isinstance(console, dict)
        ]

    def _get_input_parameters(self) -> JsonObject:
        return {}

    def _get_input_data(self) -> JsonObject:
        return {}


class GetConsoleInfo(BaseRequest[Console]):
    """ Return information about a console instance.

    Args:
        `BaseRequest (Console)`: The console object.
    """

    def __init__(self, console_id: int) -> None:
        """ Initialize the request.

        Args:
            `console_id (int)`: The id of the console to get info for.
        """
        super().__init__('consoles/{console_id}'.format(console_id=console_id),
                         RequestMethod.GET)

    def get_return_value(self, data: JsonValue) -> Console:
        if isinstance(data, dict):
            return Console(**data)
        raise ValueError(
            'Expected a dict, got {} instead.'.format(type(data)))

    def _get_input_parameters(self) -> JsonObject:
        return {}

    def _get_input_data(self) -> JsonObject:
        return {}


class KillConsole(BaseRequest[None]):
    """ Return information about a console instance.

    Args:
        `BaseRequest (None)`: Returns None.
    """

    def __init__(self, console_id: int) -> None:
        """ Initialize the request.

        Args:
            `console_id (int)`: The id of the console to kill.
        """
        super().__init__('consoles/{console_id}'.format(console_id=console_id),
                         RequestMethod.DELETE)

    def get_return_value(self, data: JsonValue) -> None:
        return None

    def _get_input_parameters(self) -> JsonObject:
        return {}

    def _get_input_data(self) -> JsonObject:
        return {}


class GetConsoleOutput(BaseRequest[str]):
    """ Get the most recent output from the console (approximately 500 characters).

    Args:
        `BaseRequest (str)`: The output from the console.
    """

    def __init__(self, console_id: int) -> None:
        """ Get the most recent output from the console (approximately 500 characters).

        Args:
            `console_id (int)`: The ID of the console to get the output from.
        """
        super().__init__('consoles/{console_id}/get_latest_output'.format(
            console_id=console_id), RequestMethod.GET)

    def get_return_value(self, data: JsonValue) -> str:
        return data["output"]  # type: ignore

    def _get_input_parameters(self) -> JsonObject:
        return {}

    def _get_input_data(self) -> JsonObject:
        return {}


class SendConsoleInput(BaseRequest[None]):
    """ "type" into the console. Add a `new-line` for return.

    Args:
        `BaseRequest (None)`: Returns None.
    """

    def __init__(self, console_id: int, input_text: str) -> None:
        """ "type" into the console. Add a `new-line` for return.

        Args:
            `console_id (int)`: The ID of the console to send the input to.
            `input_text (str)`: The input text to "type" inside console
        """
        super().__init__('consoles/{console_id}/send_input'.format(
            console_id=console_id), RequestMethod.POST)
        self._input_text = input_text

    def get_return_value(self, data: JsonValue) -> None:
        return None

    def _get_input_parameters(self) -> JsonObject:
        return {}

    def _get_input_data(self):
        return {
            'input': self._input_text
        }
