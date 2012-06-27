from collective.behavior.salable import _
from zope.interface import Interface
from zope.schema import Bool


class ISalable(Interface):
    """Interface for Salable behavior."""

    salable = Bool(
        title=_(u"Salable"),
        description=_(u"Uncheck this if not salable."),
        default=True)
