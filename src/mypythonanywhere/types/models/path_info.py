import dataclasses
import enum

from ..custom_type_alias import JsonObject


class PathType(enum.Enum):
    """
    Enum for path types.
    """
    FILE = 'file'
    DIRECTORY = 'directory'
    SYMLINK = 'symlink'


@dataclasses.dataclass(init=True, kw_only=True)
class PathInfo:
    """ Information about a path.
    """

    type: PathType
    """ The type of the path."""

    url: str
    """ The url of the path."""

    @staticmethod
    def from_result(result: JsonObject) -> 'PathInfo':
        """
        Create a PathInfo from a result.
        """
        return PathInfo(
            type=PathType(result['type']),
            url=result['url'],
        )
