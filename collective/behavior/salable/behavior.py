from collective.behavior.salable.interfaces import ISalable
from decimal import Decimal
from plone.directives import form
from rwproperty import getproperty
from rwproperty import setproperty
from zope.interface import alsoProvides
from zope.interface import implements

import logging

logger = logging.getLogger(__name__)


alsoProvides(ISalable, form.IFormFieldProvider)


class Salable(object):
    """
    """
    implements(ISalable)

    def __init__(self, context):
        self.context = context

    @getproperty
    def salable(self):
        return getattr(self.context, 'salable', True)

    @setproperty
    def salable(self, value):
        """Set salable as Boolean

        :param value: True or False
        :type value: bool
        """
        if value is not True:
            if value is not False:
                raise ValueError('Not Bool')
        setattr(self.context, 'salable', value)
