class PathNotFound(Exception):
    """
    Raised when a path is not found.
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
