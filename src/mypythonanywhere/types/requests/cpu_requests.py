import aiohttp

from ..base_request import BaseRequest
from ..custom_type_alias import JsonObject
from ..models.cpu import CpuUsage
from ..request_method import RequestMethod


class GetCpuUsage(BaseRequest[CpuUsage]):
    """
    Get the CPU usage.

    Args:
        `BaseRequest (CpuUsage)`: The CPU usage.
    """

    def __init__(self):
        """ Get the CPU usage.
        """
        super().__init__('cpu', RequestMethod.GET)

    async def get_return_value(
            self, http_response: aiohttp.ClientResponse) -> CpuUsage:

        data = await self.ensure_getting_json_response(http_response)

        if isinstance(data, dict):
            return CpuUsage(**data)
        raise ValueError("Expected a dict, got {}".format(type(data)))

    def _get_input_parameters(self) -> JsonObject:
        return {}

    def _get_input_data(self) -> JsonObject:
        return {}
