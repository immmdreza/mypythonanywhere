import abc

from ._client_acceptable import ClientAcceptable
from ._client_targetable import ClientTargetable


class MethodOutput(abc.ABC, ClientAcceptable, ClientTargetable):
    """ A class that can accept a Friendly Client. """
    pass
