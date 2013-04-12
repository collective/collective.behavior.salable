from collective.behavior.salable import _
from plone.directives import form
from zope.schema import Bool


class ISalable(form.Schema):
    """Interface for Salable behavior."""

    salable = Bool(
        title=_(u"Salable"),
        description=_(u"Uncheck this if not salable."),
        default=True)
