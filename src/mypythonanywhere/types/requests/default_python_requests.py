from ..base_request import BaseRequest
from ..custom_type_alias import JsonObject, JsonValue
from ..models.python_version import PythonVersionInfo
from ..request_method import RequestMethod


class GetDefaultPython3Request(BaseRequest[PythonVersionInfo]):
    """
    Get the default Python version.
    """

    def __init__(self) -> None:
        """
        Returns information about user's current and available default Python 3
        version
        """
        super().__init__('default_python3_version', RequestMethod.GET)

    def get_return_value(self, data: JsonValue):
        if isinstance(data, dict):
            return PythonVersionInfo(
                data['default_python3_version'],
                data['available_python3_versions'])
        raise ValueError(f'Expected dict, got {type(data)}')

    def _get_input_data(self) -> JsonObject:
        return {}

    def _get_input_parameters(self) -> JsonObject:
        return {}


class SetDefaultPython3Request(BaseRequest[PythonVersionInfo]):
    """
    Set the default Python version.
    """

    def __init__(self, default_python3_version: str) -> None:
        """
        Sets default Python 3 version for user.
        """
        super().__init__('default_python3_version', RequestMethod.PATCH)
        self._default_python3_version = default_python3_version

    def get_return_value(self, data: JsonValue):
        if isinstance(data, dict):
            return PythonVersionInfo(
                data['default_python3_version'],
                data['available_python3_versions'])
        raise ValueError(f'Expected dict, got {type(data)}')

    def _get_input_data(self) -> JsonObject:
        return {'default_python3_version': self._default_python3_version}

    def _get_input_parameters(self) -> JsonObject:
        return {}


class GetDefaultPythonRequest(BaseRequest[PythonVersionInfo]):
    """
    Get the default Python 2 version.
    """

    def __init__(self) -> None:
        """
        Returns information about user's current and available default Python
        version
        """
        super().__init__('default_python_version', RequestMethod.GET)

    def get_return_value(self, data: JsonValue):
        if isinstance(data, dict):
            return PythonVersionInfo(
                data['default_python_version'],
                data['available_python_versions'])
        raise ValueError(f'Expected dict, got {type(data)}')

    def _get_input_data(self) -> JsonObject:
        return {}

    def _get_input_parameters(self) -> JsonObject:
        return {}


class SetDefaultPythonRequest(BaseRequest[PythonVersionInfo]):
    """
    Set the default Python 2 version.
    """

    def __init__(self, default_python_version: str) -> None:
        """
        Sets default Python 2 version for user.
        """
        super().__init__('default_python_version', RequestMethod.PATCH)
        self._default_python_version = default_python_version

    def get_return_value(self, data: JsonValue):
        if isinstance(data, dict):
            return PythonVersionInfo(
                data['default_python_version'],
                data['available_python_versions'])
        raise ValueError(f'Expected dict, got {type(data)}')

    def _get_input_data(self) -> JsonObject:
        return {'default_python_version': self._default_python_version}

    def _get_input_parameters(self) -> JsonObject:
        return {}


class GetSaveAndRunDefaultPythonRequest(BaseRequest[PythonVersionInfo]):
    """
    Returns information about user's current and available Python version
    used for the "Run" button in the editor.
    """

    def __init__(self) -> None:
        """
        Returns information about user's current and available Python version
        used for the "Run" button in the editor.
        """
        super().__init__('default_save_and_run_python_version',
                         RequestMethod.GET)

    def get_return_value(self, data: JsonValue):
        if isinstance(data, dict):
            return PythonVersionInfo(
                data['default_save_and_run_python_version'],
                data['available_python_versions'])
        raise ValueError(f'Expected dict, got {type(data)}')

    def _get_input_data(self) -> JsonObject:
        return {}

    def _get_input_parameters(self) -> JsonObject:
        return {}


class SetSaveAndRunDefaultPythonRequest(BaseRequest[PythonVersionInfo]):
    """
    Set the default Python version used for the "Run" button in the editor.
    """

    def __init__(self, default_save_and_run_python_version: str) -> None:
        """
        Sets default Python version used for the "Run" button in the editor.
        """
        super().__init__('default_save_and_run_python_version',
                         RequestMethod.PATCH)
        self._default_save_and_run_python_version = default_save_and_run_python_version

    def get_return_value(self, data: JsonValue):
        if isinstance(data, dict):
            return PythonVersionInfo(
                data['default_save_and_run_python_version'],
                data['available_python_versions'])
        raise ValueError(f'Expected dict, got {type(data)}')

    def _get_input_data(self) -> JsonObject:
        return {'default_save_and_run_python_version': self._default_save_and_run_python_version}

    def _get_input_parameters(self) -> JsonObject:
        return {}
