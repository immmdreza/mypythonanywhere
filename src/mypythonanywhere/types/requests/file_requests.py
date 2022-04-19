import pathlib

from ..base_request import BaseOrder, BaseRequest
from ..custom_type_alias import JsonObject, JsonValue
from ..models.path_info import PathInfo
from ..request_method import RequestMethod


class GetPath(BaseRequest[dict[str, PathInfo]]):
    """
    Request to get all files in a directory.
    """

    def __init__(self, path: str):
        """
        :param path: The path to the directory.
        """
        super().__init__(f'files/path/{path}', RequestMethod.GET)

    def get_return_value(self, data: JsonValue) -> dict[str, PathInfo]:
        if isinstance(data, dict):
            return {
                key: PathInfo.from_result(value)
                for key, value in data.items()
            }
        raise ValueError(f'Expected a list, got {type(data)}')

    def _get_input_data(self) -> JsonObject:
        return {}

    def _get_input_parameters(self) -> JsonObject:
        return {}


class UploadFile(BaseOrder):
    """
    Upload a file to the server.
    """

    def __init__(self, file_path: pathlib.Path, upload_path: str) -> None:
        """
        Upload a file to the server.
        """
        super().__init__('files/path/{path}'.format(
            path=upload_path), RequestMethod.POST)
        self._file_path = file_path

    def _get_input_data(self) -> JsonObject:
        return {}

    def _get_input_parameters(self) -> JsonObject:
        return {}

    def _get_input_file(self) -> JsonObject:
        return {'content': open(self._file_path, 'rb')}


class GetTree(BaseRequest[list[str]]):
    """
    Request to get the tree of a directory.
    """

    def __init__(self, path: str) -> None:
        """
        :param path: The path to the directory.
        """
        super().__init__('files/tree', RequestMethod.GET)
        self._path = path

    def get_return_value(self, data: JsonValue) -> list[str]:
        if isinstance(data, list):
            return data  # type: ignore
        raise ValueError(f'Expected a list, got {type(data)}')

    def _get_input_data(self) -> JsonObject:
        return {}

    def _get_input_parameters(self) -> JsonObject:
        return {'path': self._path}


class DeleteFile(BaseOrder):
    """
    Delete a file from the server.
    """

    def __init__(self, path: str) -> None:
        """
        :param path: The path to the file.
        """
        super().__init__('files/path/{path}'.format(
            path=path), RequestMethod.DELETE)

    def _get_input_data(self) -> JsonObject:
        return {}

    def _get_input_parameters(self) -> JsonObject:
        return {}


class ShareFile(BaseOrder):
    """
    Start sharing a file.
    """

    def __init__(self, path: str) -> None:
        """
        :param path: The path to the file.
        """
        super().__init__('files/sharing', RequestMethod.POST)
        self._path = path

    def _get_input_data(self) -> JsonObject:
        return {'path': self._path}

    def _get_input_parameters(self) -> JsonObject:
        return {}
