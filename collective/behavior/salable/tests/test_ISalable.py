import unittest


class TestISalable(unittest.TestCase):

    def test_subclass(self):
        from collective.behavior.salable.interfaces import ISalable
        from zope.interface import Interface
        self.assertTrue(issubclass(ISalable, Interface))

    def get_schema(self, name):
        """Get schema by name.

        :param name: Name of schema.
        :type name: str
        """
        from collective.behavior.salable.interfaces import ISalable
        return ISalable.get(name)

    def test_salable__instance(self):
        schema = self.get_schema('salable')
        from zope.schema import Bool
        self.assertIsInstance(schema, Bool)

    def test_salable__title(self):
        schema = self.get_schema('salable')
        self.assertEqual(schema.title, u'Salable')

    def test_salable__description(self):
        schema = self.get_schema('salable')
        self.assertEqual(
            schema.description, u'Uncheck this if not salable.')

    def test_salable__default(self):
        schema = self.get_schema('salable')
        self.assertTrue(schema.default)
