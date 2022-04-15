import requests
import typing

from .types.account_type import AccountType
from .types.base_request import BaseRequest


T = typing.TypeVar('T')


class PythonAnywhereClient:
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

    def _get_host_addr(self):
        match (self._account_type):
            case AccountType.UsBased: return 'www.pythonanywhere.com'
            case AccountType.EuBased: return 'eu.pythonanywhere.com'
            case _: raise ValueError('Unknown account type')

    def _send_request(self, endpoint: str, method: str, data: dict):
        url = '{base_url}{endpoint}'.format(
            base_url=self._base_url, endpoint=endpoint
        )
        headers = {
            'Authorization': 'Token {token}'.format(token=self._token)
        }
        request = requests.Request(method, url, headers=headers, data=data)
        prepared = request.prepare()
        with requests.session() as session:
            return session.send(prepared)

    def send(self, request: BaseRequest[T]) -> T:
        """
        Send a request to the API.
        """
        response = self._send_request(
            request.method,
            request.request_method.value,
            request.get_input_parameters())

        if response.status_code != 200:
            raise ValueError(
                'Request failed with status code {status_code}'.format(
                    status_code=response.status_code
                )
            )

        json_result = response.json()
        return request.get_return_value(json_result)
