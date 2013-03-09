from collective.behavior.salable.behavior import Salable
from collective.behavior.salable.interfaces import ISalable

import mock
import unittest


class SalableTestCase(unittest.TestCase):
    """TestCase for Salable"""

    def test_subclass(self):
        self.assertTrue(issubclass(Salable, object))

    def create_instance(self, context=mock.Mock()):
        return Salable(context)

    def test_instance(self):
        instance = self.create_instance()
        self.assertIsInstance(instance, Salable)

    def test_instance_provides_ISalable(self):
        instance = self.create_instance()
        self.assertTrue(ISalable.providedBy(instance))

    def test_instance__verifyObject(self):
        instance = self.create_instance()
        from zope.interface.verify import verifyObject
        self.assertTrue(verifyObject(ISalable, instance))

    def test_salable(self):
        context = mock.Mock()
        del context.salable
        instance = self.create_instance(context=context)
        self.assertTrue(instance.salable)

    def test_instance__salable__set(self):
        context = mock.Mock()
        instance = self.create_instance(context=context)
        instance.salable = False
        self.assertFalse(instance.salable)
        self.assertFalse(instance.context.salable)

    def set_salable(self, value):
        context = mock.Mock()
        instance = self.create_instance(context=context)
        instance.salable = value

    def test_instance__salable__ValueError(self):
        self.assertRaises(ValueError, lambda: self.set_salable('AAA'))
