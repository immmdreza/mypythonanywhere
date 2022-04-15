import enum


class AccountType(enum.Enum):
    """
    Enum for account types.
    """

    UsBased = 1
    """if your account is on our US-based system."""

    EuBased = 2
    """if your account is on our EU-based system."""
