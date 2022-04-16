from ..base_request import BaseRequest
from ..request_method import RequestMethod
from ..models.cpu import CpuUsage


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

    def get_return_value(self, data) -> CpuUsage:
        return CpuUsage(**data)

    def _get_input_parameters(self):
        return {}

    def _get_input_data(self):
        return {}
