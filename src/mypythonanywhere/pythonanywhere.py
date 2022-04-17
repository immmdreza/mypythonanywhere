import typing

import requests

from .types.account_type import AccountType
from .types.base_request import BaseRequest
from .types.custom_type_alias import T
from .types.request_method import RequestMethod


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

        from .clients.always_on_client import PythonAnywhereAlwaysOnClient
        from .clients.console_client import PythonAnywhereConsoleClient
        from .clients.cpu_client import PythonAnywhereCpuClient
        from .clients.default_python_client import PythonAnywhereDefaultPythonClient

        self.cpu = PythonAnywhereCpuClient(self)
        self.consoles = PythonAnywhereConsoleClient(self)
        self.always_ons = PythonAnywhereAlwaysOnClient(self)
        self.default_python = PythonAnywhereDefaultPythonClient(self)

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
            self,
            endpoint: str,
            method: RequestMethod,
            params: dict[str, typing.Any],
            data: dict[str, typing.Any]):

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
                url, headers=headers, params=params, data=data)
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

        json_result: dict[str, typing.Any] = response.json() \
            if response.text else {}
        return request.get_return_value(json_result)
