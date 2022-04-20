import abc


class FileUploaded(abc.ABC):
    """ Abstract class for file upload result."""

    def __init__(self, existing: bool) -> None:
        super().__init__()
        self._existing = existing


class FileCreated(FileUploaded):
    """ A new file has been created."""

    def __init__(self) -> None:
        super().__init__(existing=False)


class FileUpdated(FileUploaded):
    """ A file has been updated."""

    def __init__(self) -> None:
        super().__init__(existing=True)
