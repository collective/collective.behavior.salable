from Products.CMFCore.utils import getToolByName
from collective.behavior.salable.tests.base import IntegrationTestCase


class TestSetup(IntegrationTestCase):

    def setUp(self):
        self.portal = self.layer['portal']

    def test_is_collective_behavior_salable_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(
            installer.isProductInstalled('collective.behavior.salable'))

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile(
                'profile-collective.behavior.salable:default'), u'0')

    def test_uninstall__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.behavior.salable'])
        self.failIf(installer.isProductInstalled('collective.behavior.salable'))
