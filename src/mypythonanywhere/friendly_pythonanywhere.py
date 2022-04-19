import aiohttp

from .clients.always_on_client import PythonAnywhereAlwaysOnClient
from .clients.console_client import PythonAnywhereConsoleClient
from .clients.cpu_client import PythonAnywhereCpuClient
from .clients.default_python_client import PythonAnywhereDefaultPythonClient
from .clients.file_client import PythonAnywhereFileClient
from .pythonanywhere import AccountType, PythonAnywhereClient


class FriendlyPythonAnywhereClient(PythonAnywhereClient):
    """ A friendly pythonanywhere client to communicate with the API.

    This class contains all available methods.

    Args:
        PythonAnywhereClient (_type_): PythonAnywhereClient.
    """

    def __init__(
            self, username: str, token: str, account_type: AccountType, with_session: aiohttp.ClientSession | None = None):
        super().__init__(username, token, account_type, with_session)

        self._always_on: PythonAnywhereAlwaysOnClient | None = None
        self._default_python: PythonAnywhereDefaultPythonClient | None = None
        self._console: PythonAnywhereConsoleClient | None = None
        self._cpu: PythonAnywhereCpuClient | None = None
        self._file: PythonAnywhereFileClient | None = None

    @property
    def always_on(self) -> PythonAnywhereAlwaysOnClient:
        """ Get the always_on client.

        This client contains methods related to the always on tasks.

        Returns:
            PythonAnywhereAlwaysOnClient: AlwaysOn client.
        """
        if self._always_on is None:
            self._always_on = PythonAnywhereAlwaysOnClient(self)

        return self._always_on

    @property
    def default_python(self) -> PythonAnywhereDefaultPythonClient:
        """ Get the default_python client.

        This client contains methods related to the default python.

        Returns:
            PythonAnywhereDefaultPythonClient: DefaultPython client.
        """
        if self._default_python is None:
            self._default_python = PythonAnywhereDefaultPythonClient(self)

        return self._default_python

    @property
    def console(self) -> PythonAnywhereConsoleClient:
        """ Get the console client.

        This client contains methods related to the consoles.

        Returns:
            PythonAnywhereConsoleClient: Console client.
        """
        if self._console is None:
            self._console = PythonAnywhereConsoleClient(self)

        return self._console

    @property
    def cpu(self) -> PythonAnywhereCpuClient:
        """ Get the cpu client.

        This client contains methods related to the cpu usage.

        Returns:
            PythonAnywhereCpuClient: Cpu client.
        """
        if self._cpu is None:
            self._cpu = PythonAnywhereCpuClient(self)

        return self._cpu

    @property
    def file(self) -> PythonAnywhereFileClient:
        """ Get the file client.

        This client contains methods related to the files.

        Returns:
            PythonAnywhereFileClient: File client.
        """
        if self._file is None:
            self._file = PythonAnywhereFileClient(self)

        return self._file
