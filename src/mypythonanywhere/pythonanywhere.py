import logging
from typing import Any, Optional

import aiohttp

from .types.account_type import AccountType
from .types.base_request import BaseRequest
from .types.custom_type_alias import T
from .types.request_method import RequestMethod


logger = logging.getLogger("pythonanywhere")


class PythonAnywhereClient(object):
    """
    A pythonanywhere client to communicate with the API.
    """

    def __init__(
            self,
            username: str,
            token: str,
            account_type: AccountType,
            with_session: aiohttp.ClientSession | None = None):

        self._username = username
        self._token = token
        self._account_type = account_type
        self._host_addr = self._get_host_addr()
        self._base_url = 'https://{host}/api/v0/user/{username}/'.format(
            host=self._host_addr, username=username
        )
        self._default_session = with_session

    async def __call__(
            self,
            request: BaseRequest[T],
            session: Optional[aiohttp.ClientSession] = None) -> T:
        """Sends a API request

        Args:
            request (`BaseRequest[T]`): A request to made.

        Returns:
            `T`: Return value of the request.
        """

        if self._default_session is not None:
            session = self._default_session
            logger.info("Using default session for __call__.")

        return await self._send(request, session)

    async def __aenter__(self):
        if self._default_session is None:
            logger.info("Creating new session for __aenter__.")
            self._default_session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any):
        if self._default_session is not None:
            await self._default_session.close()
            self._default_session = None
            logger.info("Closed session for __aexit__.")

    def clone_with_session(self, session: aiohttp.ClientSession) -> 'PythonAnywhereClient':
        """Clones this client with a new session.

        Args:
            session (`aiohttp.ClientSession`): The new session.

        Returns:
            `PythonAnywhereClient`: A new client with the new session.
        """

        return PythonAnywhereClient(
            username=self._username,
            token=self._token,
            account_type=self._account_type,
            with_session=session
        )

    def _get_host_addr(self):
        match (self._account_type):
            case AccountType.UsBased: return 'www.pythonanywhere.com'
            case AccountType.EuBased: return 'eu.pythonanywhere.com'
            case _: raise ValueError('Unknown account type')

    def _create_url(self, endpoint: str) -> str:
        """Creates a url for the API.

        Args:
            endpoint (`str`): The endpoint to create the url for.

        Returns:
            `str`: The url for the API.
        """

        return '{base_url}{endpoint}/'.format(
            base_url=self._base_url, endpoint=endpoint
        )

    @staticmethod
    async def _get_output(
            request: BaseRequest[T],
            response: aiohttp.ClientResponse) -> T:
        response.raise_for_status()

        if response.content_type == 'application/json':
            json_result = await response.json()
            return request.get_return_value(json_result)
        return None  # type: ignore

    async def _send(
            self,
            request: BaseRequest[T],
            session: Optional[aiohttp.ClientSession] = None) -> T:
        """Sends a API request."""

        url = self._create_url(request.method)
        one_time_session = False
        if session is None:
            session = aiohttp.ClientSession()
            one_time_session = True
            logger.info("Creating new one time session for _send.")

        if 'Authorization' not in session.headers:
            logger.info("Adding Authorization header to session.")
            session.headers['Authorization'] = \
                'Token {token}'.format(token=self._token)

        out_put: T
        match (request.request_method):
            case RequestMethod.GET:
                async with session.get(
                        url, params=request.params) as response:
                    out_put = await PythonAnywhereClient._get_output(
                        request, response)
            case RequestMethod.POST:

                kw_args = {
                    'params': request.params,
                }

                if request.data:
                    kw_args['json'] = request.data
                elif request.files:
                    kw_args['data'] = request.files

                async with session.post(url, **kw_args) as response:
                    out_put = await PythonAnywhereClient._get_output(
                        request, response)
            case RequestMethod.DELETE:
                async with session.delete(
                        url,
                        params=request.params,
                        json=request.data) as response:
                    out_put = await PythonAnywhereClient._get_output(
                        request, response)
            case RequestMethod.PATCH:
                async with session.patch(
                        url,
                        params=request.params,
                        json=request.data) as response:
                    out_put = await PythonAnywhereClient._get_output(
                        request, response)
            case _: raise ValueError('Unknown request method')

        if one_time_session:
            logger.info("Closing one time session for _send.")
            await session.close()
        return out_put
