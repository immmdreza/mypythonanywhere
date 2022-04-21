from typing import Optional

from ..pythonanywhere import PythonAnywhereClient
from ..types.models.interval_type import IntervalType
from ..types.models.schedule_task import ScheduledTask
from ..types.requests.schedule import (CreateScheduledTask,
                                       DeleteScheduledTask, GetScheduledTask,
                                       GetScheduledTasks, PatchScheduledTask,
                                       PutScheduledTask)


class PythonAnywhereScheduleClient:
    def __init__(self, raw_client: PythonAnywhereClient) -> None:
        self._raw_client = raw_client

    async def get_scheduled_tasks(self):
        """ Get the scheduled tasks. """
        request = GetScheduledTasks()
        return await self._raw_client(request)

    async def create_scheduled_task(
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
        request = CreateScheduledTask(
            command=command,
            enabled=enabled,
            interval=interval,
            hour=hour,
            minute=minute,
            description=description
        )
        return await self._raw_client(request)

    async def get_scheduled_task(self, task_id: int):
        """ Get a scheduled task.

        Args:
            task_id (`int`): The task id.
        """
        request = GetScheduledTask(task_id=task_id)
        return await self._raw_client(request)

    async def delete_scheduled_task(self, task_id: int):
        """ Delete a scheduled task.

        Args:
            task_id (`int`): The task id.
        """
        request = DeleteScheduledTask(task_id=task_id)
        return await self._raw_client(request)

    async def patch_scheduled_task(self, scheduled_task: ScheduledTask):
        """ Patch a scheduled task.

        Args:
            scheduled_task (`ScheduledTask`): The scheduled task.
        """
        request = PatchScheduledTask(scheduled_task=scheduled_task)
        return await self._raw_client(request)

    async def put_scheduled_task(self, scheduled_task: ScheduledTask):
        """ Put a scheduled task.

        Args:
            scheduled_task (`ScheduledTask`): The scheduled task.
        """
        request = PutScheduledTask(scheduled_task=scheduled_task)
        return await self._raw_client(request)
