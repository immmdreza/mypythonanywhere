from ..types.requests.cpu import GetCpuUsage
from ..pythonanywhere import PythonAnywhereClient


class PythonAnywhereCpuClient:
    def __init__(self, raw_client: PythonAnywhereClient) -> None:
        self._raw_client = raw_client

    async def get_cpu_usage(self):
        """ Get the CPU usage of the server. """
        request = GetCpuUsage()
        return await self._raw_client(request)
