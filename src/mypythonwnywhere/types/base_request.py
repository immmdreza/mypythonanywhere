import abc
from .request_method import RequestMethod
import typing


T = typing.TypeVar('T')


class BaseRequest(abc.ABC, typing.Generic[T]):
    def __init__(self, method: str, request_method: RequestMethod) -> None:
        super().__init__()
        self._method = method
        self._request_method = request_method

    @property
    def method(self):
        return self._method

    @property
    def request_method(self):
        return self._request_method

    @abc.abstractmethod
    def get_return_value(self, data: dict[str, typing.Any] | list) -> T:
        ...

    @abc.abstractmethod
    def get_input_parameters(self) -> typing.Dict[str, typing.Any]:
        ...
