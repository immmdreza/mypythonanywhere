import typing


JsonObject: typing.TypeAlias = dict[str, typing.Any]
JsonList: typing.TypeAlias = list[JsonObject]
JsonValue: typing.TypeAlias = JsonObject | JsonList
T = typing.TypeVar('T')
