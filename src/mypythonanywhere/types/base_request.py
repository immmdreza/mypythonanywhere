import abc
import typing

from ..types.custom_type_alias import JsonObject, JsonValue, T
from .request_method import RequestMethod


class BaseRequest(abc.ABC, typing.Generic[T]):
    def __init__(self, method: str, request_method: RequestMethod) -> None:
        """ BaseRequest

        Args:
            method (str): The method name.
            request_method (RequestMethod): The request method.
        """
        super().__init__()
        self._method = method
        self._request_method = request_method

    @property
    def method(self):
        """ The method name of the request."""
        return self._method

    @property
    def request_method(self):
        """ The request method of the request."""
        return self._request_method

    @abc.abstractmethod
    def get_return_value(self, data: JsonValue) -> T:
        """ Get the return value of the request.

        Args:
            data (JsonValue): The data returned by the request.

        Returns:
            T: The return value of the request.
        """
        ...

    @abc.abstractmethod
    def _get_input_parameters(self) -> JsonObject:
        """ Get the input parameters of the request.

        Returns:
            JsonObject: The input parameters of the request.
        """
        ...

    @abc.abstractmethod
    def _get_input_data(self) -> JsonObject:
        """ Get the input data of the request.

        Returns:
            JsonObject: The input data of the request.
        """
        ...

    @property
    def params(self):
        """ The input parameters of the request."""
        params = self._get_input_parameters()
        return {k: v for k, v in params.items() if v is not None}

    @property
    def data(self):
        """ The input data of the request.

        Returns:
            JsonObject: The input data of the request.
        """
        data = self._get_input_data()
        return {k: v for k, v in data.items() if v is not None}
