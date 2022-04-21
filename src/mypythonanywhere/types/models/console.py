import dataclasses

from ...types import MethodOutput


@dataclasses.dataclass(init=True, kw_only=True)
class Console(MethodOutput):
    """
    Represents information about a console instance.
    """

    id: int
    """ The id of the console. """

    user: str
    """ The user that owns the console. """

    executable: str
    """ The executable that is running on the console. """

    arguments: str
    """ The arguments that are passed to the executable. """

    working_directory: str | None
    """ The working directory that the executable is running in. """

    name: str
    """ The name of the console. """

    console_url: str
    """ The url of the console. """

    console_frame_url: str
    """ The url of the console frame. """

    async def kill(self) -> None:
        """
        Kill the console.
        """
        await self.client.console.kill_console(self.id)
