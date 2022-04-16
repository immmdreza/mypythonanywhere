import dataclasses


@dataclasses.dataclass(init=True, frozen=True, kw_only=True)
class CpuUsage:
    """
    Represents information about a CPU usage.
    """

    daily_cpu_limit_seconds: int
    """ The number of seconds the CPU can be used per day. """

    next_reset_time: str
    """ The time the next reset will occur. """

    daily_cpu_total_usage_seconds: float
    """ The number of seconds the CPU has been used today. """
