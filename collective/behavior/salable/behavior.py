from collective.behavior.salable.interfaces import ISalable
from decimal import Decimal
from plone.directives import form
from zope.interface import alsoProvides
from zope.interface import implements


alsoProvides(ISalable, form.IFormFieldProvider)


class Salable(object):
    """
    """
    implements(ISalable)

    def __init__(self, context):
        self.context = context

    @property
    def salable(self):
        return getattr(self.context, 'salable', True)

    @salable.setter
    def salable(self, value):
        """Set salable as Boolean

        :param value: True or False
        :type value: bool
        """
        if not isinstance(value, bool):
            raise ValueError('Not Bool')
        setattr(self.context, 'salable', value)
