import abc


class FileShared(abc.ABC):
    """ Abstract class for file share result."""

    def __init__(self, already_sharing: bool) -> None:
        super().__init__()
        self._already_sharing = already_sharing


class FileAlreadyShared(FileShared):
    """ A file is already shared."""

    def __init__(self) -> None:
        super().__init__(already_sharing=True)


class FileStartedSharing(FileShared):
    """ A file has been started sharing."""

    def __init__(self) -> None:
        super().__init__(already_sharing=False)
