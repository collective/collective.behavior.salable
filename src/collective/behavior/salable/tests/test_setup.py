from Products.CMFCore.utils import getToolByName
from collective.behavior.salable.tests.base import IntegrationTestCase


class TestSetup(IntegrationTestCase):

    def setUp(self):
        self.portal = self.layer['portal']

    def test_is_collective_behavior_salable_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(
            installer.isProductInstalled('collective.behavior.salable'))

    def test_catalog__index__salable__instance(self):
        from Products.PluginIndexes.FieldIndex.FieldIndex import FieldIndex
        catalog = getToolByName(self.portal, 'portal_catalog')
        self.assertIsInstance(catalog.Indexes['salable'], FieldIndex)

    def test_catalog__index__salable__indexed_attrs(self):
        catalog = getToolByName(self.portal, 'portal_catalog')
        self.assertEqual(catalog.Indexes['salable'].indexed_attrs, ['salable'])

    def test_catalog__column__salable(self):
        catalog = getToolByName(self.portal, 'portal_catalog')
        self.assertIn('salable', catalog.schema())

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(setup.getVersionForProfile(
            'profile-collective.behavior.salable:default'), u'1')

    def test_uninstall__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.behavior.salable'])
        self.failIf(installer.isProductInstalled('collective.behavior.salable'))
