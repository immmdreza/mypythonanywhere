import dataclasses


@dataclasses.dataclass(init=True, frozen=True, kw_only=True)
class Console:
    id: int
    user: str
    executable: str
    arguments: str
    working_directory: str | None
    name: str
    console_url: str
    console_frame_url: str
