from pathlib import Path
from ..pythonanywhere import PythonAnywhereClient
from ..types.requests.file_requests import (DeleteFile, GetPath, GetTree,
                                            UploadFile)


class PythonAnywhereFileClient:
    def __init__(self, raw_client: PythonAnywhereClient) -> None:
        self._raw_client = raw_client

    async def get_tree(self, path: str):
        """ Get the files and folders in a path. """
        request = GetTree(path)
        return await self._raw_client(request)

    async def get_path(self, path: str):
        """ Get the files and folders in a path. """
        request = GetPath(path)
        return await self._raw_client(request)

    async def upload_file(self, file_path: Path, destination_path: str) -> None:
        """ Upload a file to the server. """
        request = UploadFile(file_path, destination_path)
        return await self._raw_client(request)

    async def delete_file(self, path: str) -> None:
        """ Delete a file from the server. """
        request = DeleteFile(path)
        return await self._raw_client(request)
