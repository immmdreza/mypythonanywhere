from ..types.requests.default_python_requests import (
    GetDefaultPython3Request, GetDefaultPythonRequest,
    GetSaveAndRunDefaultPythonRequest, SetDefaultPython3Request,
    SetDefaultPythonRequest, SetSaveAndRunDefaultPythonRequest)
from ..pythonanywhere import PythonAnywhereClient


class PythonAnywhereDefaultPythonClient:
    def __init__(self, raw_client: PythonAnywhereClient) -> None:
        self._raw_client = raw_client

    def get_default_python(self):
        """ Get the default Python version. """
        request = GetDefaultPythonRequest()
        return self._raw_client(request)

    def set_default_python(self, default_python_version: str):
        """ Set the default Python version. """
        request = SetDefaultPythonRequest(default_python_version)
        return self._raw_client(request)

    def get_default_python3(self):
        """ Get the default Python 3 version. """
        request = GetDefaultPython3Request()
        return self._raw_client(request)

    def set_default_python3(self, default_python3_version: str):
        """ Set the default Python 3 version. """
        request = SetDefaultPython3Request(default_python3_version)
        return self._raw_client(request)

    def get_save_and_run_default_python(self):
        """ Get whether the default Python version should be saved and run. """
        request = GetSaveAndRunDefaultPythonRequest()
        return self._raw_client(request)

    def set_save_and_run_default_python(self, save_and_run_default_python: str):
        """ Set whether the default Python version should be saved and run. """
        request = SetSaveAndRunDefaultPythonRequest(
            save_and_run_default_python)
        return self._raw_client(request)
