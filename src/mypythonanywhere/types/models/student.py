import dataclasses

from ...types import MethodOutput


@dataclasses.dataclass(init=True, kw_only=True)
class Student(MethodOutput):
    """ Student. """

    username: str
    """ The username. """
