from ..base_request import BaseRequest
from ..custom_type_alias import JsonObject, JsonValue
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

    def get_return_value(self, data: JsonValue) -> CpuUsage:
        if isinstance(data, dict):
            return CpuUsage(**data)
        raise ValueError("Expected a dict, got {}".format(type(data)))

    def _get_input_parameters(self) -> JsonObject:
        return {}

    def _get_input_data(self) -> JsonObject:
        return {}
