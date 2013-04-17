from collective.behavior.salable import _
from plone.supermodel.model import Schema
from zope import schema


class SalableSchema(Schema):
    """Schema for behavior: Salable"""

    salable = schema.Bool(
        title=_(u"Salable"),
        description=_(u"Uncheck this if not salable."),
        default=True)
