from collective.behavior.salable.interfaces import ISalable
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.interface import implements


alsoProvides(ISalable, IFormFieldProvider)


class Salable(object):
    """Behavior: Salable"""

    implements(ISalable)

    def __init__(self, context):
        self.context = context

    @property
    def salable(self):
        if not hasattr(self.context, 'salable'):
            setattr(self.context, 'salable', True)
        return getattr(self.context, 'salable')

    @salable.setter
    def salable(self, value):
        """Set salable as Boolean

        :param value: True or False
        :type value: bool
        """
        if not isinstance(value, bool):
            raise ValueError('Not Bool')
        setattr(self.context, 'salable', value)
