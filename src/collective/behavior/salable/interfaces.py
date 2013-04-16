from collective.behavior.salable import _
from zope import schema
from zope.interface import Interface


class ISalable(Interface):
    """Interface for Salable behavior."""

    salable = schema.Bool(
        title=_(u"Salable"),
        description=_(u"Uncheck this if not salable."),
        default=True)
