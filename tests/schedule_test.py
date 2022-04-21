import logging
import sys
import unittest

from src.mypythonanywhere import AccountType, FriendlyPythonAnywhereClient
from src.mypythonanywhere.types.models.interval_type import IntervalType
from src.mypythonanywhere.types.requests.schedule import (CreateScheduledTask,
                                                          GetScheduledTasks,
                                                          DeleteScheduledTask,
                                                          GetScheduledTask,
                                                          PutScheduledTask)

from helpers import load_account_details_from_env

logging.basicConfig(level=logging.INFO, handlers=[
    logging.StreamHandler(sys.stdout)
])


class ScheduleTest(unittest.IsolatedAsyncioTestCase):

    def setUp(self) -> None:
        (username, token, account_type) = load_account_details_from_env()

        self.client = FriendlyPythonAnywhereClient(
            username=username,
            token=token,
            account_type=AccountType(account_type)
        )

    async def test_get_scheduled_tasks(self):
        tasks = await self.client(GetScheduledTasks())

        self.assertTrue(isinstance(tasks, list))  # type: ignore

    async def test_create_scheduled_task(self):
        async with self.client:
            tasks = await self.client(GetScheduledTasks())
            for x in tasks:
                # delete it
                await self.client(DeleteScheduledTask(x.id))

            await self.client(CreateScheduledTask(
                command="echo 'Hello World'",
                interval=IntervalType.Daily,
                hour=12,
                minute=30,
                description="Test task"
            ))

    async def test_put_scheduled_task(self):
        task = await self.client(GetScheduledTasks())

        task = task[0]
        current_enabled = task.enabled
        task.enabled = not current_enabled

        _ = await self.client(PutScheduledTask(task))
        updated_task = await self.client(GetScheduledTask(task.id))

        self.assertTrue(updated_task.enabled != current_enabled)


if __name__ == '__main__':
    unittest.main()
