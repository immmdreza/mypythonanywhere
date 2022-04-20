import pathlib

import aiohttp

from ...exceptions.files_exceptions import PathNotFound
from ..base_request import BaseOrder, BaseRequest
from ..custom_type_alias import JsonObject
from ..models.file_shared import (FileAlreadyShared, FileShared,
                                  FileStartedSharing)
from ..models.file_uploaded import FileCreated, FileUpdated, FileUploaded
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

    async def get_return_value(
            self, http_response: aiohttp.ClientResponse) -> dict[str, PathInfo]:

        data = await self.ensure_getting_json_response(http_response)
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


class UploadFile(BaseRequest[FileUploaded]):
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

    async def get_return_value(self, http_response: aiohttp.ClientResponse):
        if http_response.status == 201:
            return FileCreated()
        elif http_response.status == 200:
            return FileUpdated()
        elif http_response.status == 404:
            raise PathNotFound()
        raise ValueError(f'Expected 201 or 200, got {http_response.status}')

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

    async def get_return_value(
            self, http_response: aiohttp.ClientResponse) -> list[str]:

        data = await self.ensure_getting_json_response(http_response)
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


class ShareFile(BaseRequest[FileShared]):
    """
    Start sharing a file.
    """

    def __init__(self, path: str) -> None:
        """
        :param path: The path to the file.
        """
        super().__init__('files/sharing', RequestMethod.POST)
        self._path = path

    async def get_return_value(self, http_response: aiohttp.ClientResponse):
        if http_response.status == 200:
            return FileStartedSharing()
        elif http_response.status == 201:
            return FileAlreadyShared()
        elif http_response.status == 404:
            raise PathNotFound()
        raise ValueError(f'Expected 201 or 200, got {http_response.status}')

    def _get_input_data(self) -> JsonObject:
        return {'path': self._path}

    def _get_input_parameters(self) -> JsonObject:
        return {}


class CheckSharingStatus(BaseRequest[bool]):
    """
    Check the sharing status of a file.
    """

    def __init__(self, path: str) -> None:
        """
        :param path: The path to the file.
        """
        super().__init__('files/sharing', RequestMethod.GET)
        self._path = path

    async def get_return_value(
            self, http_response: aiohttp.ClientResponse):

        if http_response.status == 404:
            return False
        http_response.raise_for_status()
        return True

    def _get_input_data(self) -> JsonObject:
        return {}

    def _get_input_parameters(self) -> JsonObject:
        return {'path': self._path}


class StopSharing(BaseRequest[bool]):
    """
    Stop sharing a file.
    """

    def __init__(self, path: str) -> None:
        """
        :param path: The path to the file.
        """
        super().__init__('files/sharing', RequestMethod.DELETE)
        self._path = path

    async def get_return_value(self, http_response: aiohttp.ClientResponse):
        if http_response.status == 204:
            return True
        http_response.raise_for_status()
        return False

    def _get_input_data(self) -> JsonObject:
        return {}

    def _get_input_parameters(self) -> JsonObject:
        return {'path': self._path}
