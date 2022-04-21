import aiohttp

from ..base_request import BaseRequest
from ..custom_type_alias import JsonObject
from ..request_method import RequestMethod
from ..models.system_image import SystemImageInfo


class GetSystemImageInfo(BaseRequest[SystemImageInfo]):
    """
    Get the system image info.
    """

    def __init__(self):
        """ Get the system image info.
        """
        super().__init__('system_image', RequestMethod.GET)

    async def get_return_value(
            self, http_response: aiohttp.ClientResponse) -> SystemImageInfo:

        data = await self.ensure_getting_json_response(http_response)

        if isinstance(data, dict):
            return SystemImageInfo(**data)
        raise ValueError("Expected a dict, got {}".format(type(data)))

    def _get_input_parameters(self) -> JsonObject:
        return {}

    def _get_input_data(self) -> JsonObject:
        return {}


class SetSystemImage(BaseRequest[SystemImageInfo]):
    """
    Set the system image.
    """

    def __init__(self, system_image: SystemImageInfo):
        """ Set the system image.
        Args:
            system_image (`SystemImageInfo`): The system image.
        """
        super().__init__('system_image', RequestMethod.PATCH)
        self._system_image = system_image

    async def get_return_value(
            self, http_response: aiohttp.ClientResponse):

        data = await self.ensure_getting_json_response(http_response)

        if isinstance(data, dict):
            return SystemImageInfo(**data)
        raise ValueError("Expected a dict, got {}".format(type(data)))

    def _get_input_parameters(self) -> JsonObject:
        return {}

    def _get_input_data(self) -> JsonObject:
        return {
            'system_image': self._system_image.to_json()
        }
