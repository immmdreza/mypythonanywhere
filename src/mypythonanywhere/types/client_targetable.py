from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..friendly_pythonanywhere import FriendlyPythonAnywhereClient


# We use this to get client attr.
# You should use this along with ClientAcceptable to have the attr available.
class ClientTargetable:
    """ A class that can be used as a target for a Client. """

    @property
    def client(self) -> 'FriendlyPythonAnywhereClient':
        if not hasattr(self, '_friendly_pythonanywhere_client'):
            raise AttributeError(
                'The client attribute is not set. '
                'Are you using a friendly client?'
            )
        return getattr(self, '_friendly_pythonanywhere_client')
