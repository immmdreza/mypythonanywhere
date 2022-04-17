from .pythonanywhere import PythonAnywhereClient, AccountType
from .clients.always_on_client import PythonAnywhereAlwaysOnClient
from .clients.default_python_client import PythonAnywhereDefaultPythonClient
from .clients.console_client import PythonAnywhereConsoleClient
from .clients.cpu_client import PythonAnywhereCpuClient


class FriendlyPythonAnywhereClient(PythonAnywhereClient):
    """ A friendly pythonanywhere client to communicate with the API.

    This class contains all available methods.

    Args:
        PythonAnywhereClient (_type_): PythonAnywhereClient.
    """

    def __init__(self, username: str, token: str, account_type: AccountType):
        super().__init__(username, token, account_type)

        self.always_on = PythonAnywhereAlwaysOnClient(self)
        self.default_python = PythonAnywhereDefaultPythonClient(self)
        self.console = PythonAnywhereConsoleClient(self)
        self.cpu = PythonAnywhereCpuClient(self)
