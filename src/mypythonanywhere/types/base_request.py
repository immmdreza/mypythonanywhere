import abc
import typing

import aiohttp

from ..exceptions.api_exception import ApiException
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
    async def get_return_value(self, http_response: aiohttp.ClientResponse) -> T:
        """ Get the return value of the request.

        Args:
            http_response (`aiohttp.ClientResponse`): The response of the request.

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

    def _get_input_file(self) -> JsonObject:
        return {}

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

    @property
    def files(self):
        """ The input files of the request.

        Returns:
            JsonObject: The input files of the request.
        """
        return self._get_input_file()

    @classmethod
    async def ensure_getting_json_response(
            cls, response: aiohttp.ClientResponse) -> JsonValue:
        """ Ensure that the response is a json response.

        Args:
            response (`aiohttp.ClientResponse`): The response of the request.

        Raises:
            ValueError: If the response is not a json response.
        """
        if response.content_type != 'application/json':

            response.raise_for_status()
        json = await response.json()

        if not response.ok:
            raise ApiException(
                ', '.join(f"{k}: {v}" for k, v in json.items()))

        return json


class BaseOrder(BaseRequest[None]):
    def __init__(self, method: str, request_method: RequestMethod) -> None:
        super().__init__(method, request_method)

    async def get_return_value(self, http_response: aiohttp.ClientResponse):
        return None

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
