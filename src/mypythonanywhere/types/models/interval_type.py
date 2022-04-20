import enum


class IntervalType(enum.Enum):
    """
    Enum for interval types.
    """

    Daily = "daily"
    """ Daily interval type. """

    Hourly = "hourly"
    """ Hourly interval type. """
