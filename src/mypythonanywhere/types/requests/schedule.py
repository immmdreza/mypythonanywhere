from typing import Optional
import aiohttp

from ..base_request import BaseOrder, BaseRequest
from ..custom_type_alias import JsonObject
from ..request_method import RequestMethod
from ..models.interval_type import IntervalType
from ..models.schedule_task import ScheduledTask


class GetScheduledTasks(BaseRequest[list[ScheduledTask]]):
    """
    Get the scheduled tasks.
    """

    def __init__(self):
        """ Get the scheduled tasks.
        """
        super().__init__('schedule', RequestMethod.GET)

    async def get_return_value(
            self, http_response: aiohttp.ClientResponse):

        data = await self.ensure_getting_json_response(http_response)

        if isinstance(data, list):
            return [ScheduledTask(**task) for task in data]
        raise ValueError("Expected a dict, got {}".format(type(data)))

    def _get_input_parameters(self) -> JsonObject:
        return {}

    def _get_input_data(self) -> JsonObject:
        return {}


class CreateScheduledTask(BaseRequest[ScheduledTask]):
    """
    Create a scheduled task.
    """

    def __init__(
            self,
            command: str,
            *,
            enabled: bool = True,
            interval: IntervalType = IntervalType.Daily,
            hour: Optional[int] = None,
            minute: Optional[int] = None,
            description: Optional[str] = None):
        """ Create a scheduled task.

        Args:
            command (`str`): The command to run. For example `python3.9 /home/user/my_script.py`.
            enabled (`bool`): Whether the task is enabled.
            interval (`int`): The interval in seconds.
            hour (`int`): The hour of the day. for daily tasks.
            minute (`int`): The minute of the hour. for daily tasks.
            description (`Optional[str]`, optional): Defaults to None.
        """

        super().__init__('schedule', RequestMethod.POST)
        self.command = command
        self.enabled = int(enabled)
        self.interval = interval.value
        self.hour = hour
        self.minute = minute
        self.description = description

    async def get_return_value(
            self, http_response: aiohttp.ClientResponse):

        data = await self.ensure_getting_json_response(http_response)

        if isinstance(data, dict):
            return ScheduledTask(**data)
        raise ValueError("Expected a dict, got {}".format(type(data)))

    def _get_input_parameters(self) -> JsonObject:
        return {}

    def _get_input_data(self) -> JsonObject:
        return {
            'command': self.command,
            'enabled': self.enabled,
            'interval': self.interval,
            'hour': self.hour,
            'minute': self.minute,
            'description': self.description,
        }


class GetScheduledTask(BaseRequest[ScheduledTask]):
    """
    Return information about a scheduled task.
    """

    def __init__(self, task_id: int):
        """ Return information about a scheduled task.

        Args:
            task_id (`int`): The ID of the scheduled task.
        """

        super().__init__('schedule/{}'.format(task_id), RequestMethod.GET)

    async def get_return_value(
            self, http_response: aiohttp.ClientResponse):

        data = await self.ensure_getting_json_response(http_response)

        if isinstance(data, dict):
            return ScheduledTask(**data)
        raise ValueError("Expected a dict, got {}".format(type(data)))

    def _get_input_parameters(self) -> JsonObject:
        return {}

    def _get_input_data(self) -> JsonObject:
        return {}


class DeleteScheduledTask(BaseOrder):
    """
    Delete a scheduled task.
    """

    def __init__(self, task_id: int):
        """ Delete a scheduled task.

        Args:
            task_id (`int`): The ID of the scheduled task.
        """

        super().__init__('schedule/{}'.format(task_id), RequestMethod.DELETE)

    def _get_input_parameters(self) -> JsonObject:
        return {}

    def _get_input_data(self) -> JsonObject:
        return {}


class PatchScheduledTask(BaseRequest[ScheduledTask]):
    """
    Update a scheduled task.
    """

    def __init__(self, scheduled_task: ScheduledTask):
        """ Update a scheduled task.
        """

        super().__init__(
            'schedule/{}'.format(scheduled_task.id), RequestMethod.PATCH)
        self._schedule_task = scheduled_task

    async def get_return_value(
            self, http_response: aiohttp.ClientResponse):

        data = await self.ensure_getting_json_response(http_response)

        if isinstance(data, dict):
            return ScheduledTask(**data)
        raise ValueError("Expected a dict, got {}".format(type(data)))

    def _get_input_parameters(self) -> JsonObject:
        return {}

    def _get_input_data(self) -> JsonObject:
        return self._schedule_task.to_json()


class PutScheduledTask(BaseRequest[ScheduledTask]):
    """
    Update a scheduled task.
    """

    def __init__(self, scheduled_task: ScheduledTask):
        """ Update a scheduled task.
        """

        super().__init__(
            'schedule/{}'.format(scheduled_task.id), RequestMethod.PUT)
        self._schedule_task = scheduled_task

    async def get_return_value(
            self, http_response: aiohttp.ClientResponse):

        data = await self.ensure_getting_json_response(http_response)

        if isinstance(data, dict):
            return ScheduledTask(**data)
        raise ValueError("Expected a dict, got {}".format(type(data)))

    def _get_input_parameters(self) -> JsonObject:
        return {}

    def _get_input_data(self) -> JsonObject:
        return self._schedule_task.to_json()
