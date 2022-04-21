class ApiException(Exception):
    """
    Base class for all API exceptions.
    """

    def __init__(self, details: str) -> None:
        super().__init__(details)
