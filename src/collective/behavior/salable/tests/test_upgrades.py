from Products.CMFCore.utils import getToolByName
from collective.behavior.salable.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for upgrade steps."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_update_catalog(self):
        from Products.PluginIndexes.FieldIndex.FieldIndex import FieldIndex

        catalog = getToolByName(self.portal, 'portal_catalog')
        catalog.delColumn('salable')
        catalog.delIndex('salable')
        self.assertIsNone(catalog.Indexes.get('salable'))
        self.assertNotIn('salable', catalog.schema())

        from collective.behavior.salable.upgrades import update_catalog
        update_catalog(self.portal)

        self.assertIsInstance(catalog.Indexes['salable'], FieldIndex)
        self.assertEqual(catalog.Indexes['salable'].indexed_attrs, ['salable'])
        self.assertIn('salable', catalog.schema())
