from ..types.requests.cpu_requests import GetCpuUsage
from ..pythonanywhere import PythonAnywhereClient


class PythonAnywhereCpuClient:
    def __init__(self, raw_client: PythonAnywhereClient) -> None:
        self._raw_client = raw_client

    def get_cpu_usage(self):
        """ Get the CPU usage of the server. """
        request = GetCpuUsage()
        return self._raw_client(request)
