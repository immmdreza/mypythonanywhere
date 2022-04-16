import enum


class RequestMethod(enum.Enum):
    """
    Enum for request methods.
    """

    GET = "GET"
    """if you want to get data from the server."""

    POST = "POST"
    """if you want to post data to the server."""

    PUT = "PUT"
    """if you want to put data to the server."""

    DELETE = "DELETE"
    """if you want to delete data from the server."""

    HEAD = "HEAD"
    """if you want to get headers from the server."""

    OPTIONS = "OPTIONS"
    """if you want to get options from the server."""

    CONNECT = "CONNECT"
    """if you want to connect to the server."""

    TRACE = "TRACE"
    """if you want to trace the server."""

    PATCH = "PATCH"
    """if you want to patch the server."""
