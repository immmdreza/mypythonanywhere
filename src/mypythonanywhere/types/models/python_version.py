import dataclasses


@dataclasses.dataclass(init=True)
class PythonVersionInfo:
    """
    Python version information.
    """
    default_version: str
    """ The default version of Python. """

    available_versions: list[str]
    """ The available versions of Python. """
