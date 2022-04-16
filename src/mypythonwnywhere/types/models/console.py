import dataclasses


@dataclasses.dataclass(init=True, frozen=True, kw_only=True)
class Console:
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
