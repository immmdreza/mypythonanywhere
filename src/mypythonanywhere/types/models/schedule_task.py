import dataclasses

from ..custom_type_alias import JsonObject


@dataclasses.dataclass(init=True, kw_only=True)
class ScheduledTask:
    """ A scheduled task. """

    id: int
    """ The ID of the scheduled task. """
    url: str
    """ The URL of the scheduled task. """
    user: str
    """ The user who owns the scheduled task. """
    command: str
    """ The command to run. """
    expiry: str
    """ The expiry date of the scheduled task. """
    enabled: bool
    """ Whether the task is enabled. """
    logfile: str
    """ The logfile of the scheduled task. """
    extend_url: str
    """ The URL to extend the scheduled task. """
    interval: str
    """ The interval of the scheduled task. """
    hour: int
    """ The hour of the day. """
    minute: int
    """ The minute of the hour. """
    printable_time: str
    """ The printable time of the scheduled task. """
    can_enable: bool
    """ Whether the task can be enabled. """
    description: str
    """ The description of the scheduled task. """

    def to_json(self) -> JsonObject:
        """ Convert the scheduled task to a JSON object. """
        return {
            'id': self.id,
            'url': self.url,
            'user': self.user,
            'command': self.command,
            'expiry': self.expiry,
            'enabled': self.enabled,
            'logfile': self.logfile,
            'extend_url': self.extend_url,
            'interval': self.interval,
            'hour': self.hour,
            'minute': self.minute,
            'printable_time': self.printable_time,
            'can_enable': self.can_enable,
            'description': self.description
        }
