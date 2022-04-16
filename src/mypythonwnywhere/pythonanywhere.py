import typing

import requests

from .clients import (PythonAnywhereAlwaysOnClient,
                      PythonAnywhereConsoleClient, PythonAnywhereCpuClient)
from .types.account_type import AccountType
from .types.base_request import BaseRequest
from .types.request_method import RequestMethod

T = typing.TypeVar('T')


class PythonAnywhereClient(object):
    """
    A pythonanywhere client to communicate with the API.
    """

    def __init__(
            self, username: str, token: str, account_type: AccountType):

        self._username = username
        self._token = token
        self._account_type = account_type
        self._host_addr = self._get_host_addr()
        self._base_url = 'https://{host}/api/v0/user/{username}/'.format(
            host=self._host_addr, username=username
        )

        self.cpu = PythonAnywhereCpuClient(self)
        self.consoles = PythonAnywhereConsoleClient(self)
        self.always_ons = PythonAnywhereAlwaysOnClient(self)

    def __call__(self, request: BaseRequest[T]) -> T:
        """Sends a API request

        Args:
            request (`BaseRequest[T]`): A request to made.

        Returns:
            `T`: Return value of the request.
        """

        return self._send(request)

    def _get_host_addr(self):
        match (self._account_type):
            case AccountType.UsBased: return 'www.pythonanywhere.com'
            case AccountType.EuBased: return 'eu.pythonanywhere.com'
            case _: raise ValueError('Unknown account type')

    def _send_request(
            self, endpoint: str, method: RequestMethod, params: dict, data: dict):

        url = '{base_url}{endpoint}/'.format(
            base_url=self._base_url, endpoint=endpoint
        )
        headers = {
            'Authorization': 'Token {token}'.format(token=self._token)
        }

        match (method):
            case RequestMethod.GET: return requests.get(
                url, headers=headers, params=params)
            case RequestMethod.POST: return requests.post(
                url, headers=headers, data=data, params=params)
            case RequestMethod.DELETE: return requests.delete(
                url, headers=headers, params=params, data=data)
            case RequestMethod.PATCH: return requests.patch(
                url, headers=headers, params=params)
            case _: raise ValueError('Unknown request method')

    def _send(self, request: BaseRequest[T]) -> T:
        """
        Send a request to the API.
        """
        response = self._send_request(
            request.method,
            request.request_method,
            request.params,
            request.data)

        response.raise_for_status()

        json_result = response.json() if response.text else {}
        return request.get_return_value(json_result)
