import pathlib
from ..base_request import BaseRequest
from ..custom_type_alias import JsonObject, JsonValue
from ..request_method import RequestMethod


class UploadFile(BaseRequest[JsonObject]):
    """
    Upload a file to the server.
    """

    def __init__(self, file_path: pathlib.Path, upload_path: str) -> None:
        """
        Upload a file to the server.
        """
        super().__init__('files/path{path}'.format(
            path=upload_path), RequestMethod.POST)
        self._file_path = file_path

    def get_return_value(self, data: JsonValue):
        if isinstance(data, dict):
            return data
        raise ValueError(f'Expected dict, got {type(data)}')

    def _get_input_data(self) -> JsonObject:
        return {}

    def _get_input_parameters(self) -> JsonObject:
        return {}

    def _get_input_file(self) -> JsonObject:
        return {'file': open(self._file_path, 'rb')}
