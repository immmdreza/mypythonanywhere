import aiohttp

from ..base_request import BaseOrder, BaseRequest
from ..custom_type_alias import JsonObject
from ..request_method import RequestMethod
from ..models.student import Student


class GetStudents(BaseRequest[list[Student]]):
    """
    Get the students.
    """

    def __init__(self):
        """ Get the students.
        """
        super().__init__('students', RequestMethod.GET)

    async def get_return_value(
            self, http_response: aiohttp.ClientResponse) -> list[Student]:

        data = await self.ensure_getting_json_response(http_response)

        if isinstance(data, dict):
            return [Student(**student) for student in data['students']]
        raise ValueError("Expected a list, got {}".format(type(data)))

    def _get_input_parameters(self) -> JsonObject:
        return {}

    def _get_input_data(self) -> JsonObject:
        return {}


class DeleteStudent(BaseOrder):
    """
    Delete a student.
    """

    def __init__(self, username: str):
        """ Delete a student.
        """
        super().__init__(
            'students/{username}'.format(username=username), RequestMethod.DELETE)

    async def get_return_value(
            self, http_response: aiohttp.ClientResponse) -> None:

        data = await self.ensure_getting_json_response(http_response)

        if isinstance(data, dict):
            return None
        raise ValueError("Expected a dict, got {}".format(type(data)))

    def _get_input_parameters(self) -> JsonObject:
        return {}

    def _get_input_data(self) -> JsonObject:
        return {}
