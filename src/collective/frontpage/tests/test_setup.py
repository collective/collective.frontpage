# -*- coding: utf-8 -*-
"""Setup tests for this package."""

from collective.frontpage.testing import COLLECTIVE_FRONTPAGE_INTEGRATION_TESTING  # noqa: 501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.frontpage is properly installed."""

    layer = COLLECTIVE_FRONTPAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if collective.frontpage is installed."""
        self.assertTrue(self.installer.isProductInstalled("collective.frontpage"))

    def test_browserlayer(self):
        """Test that ICollectiveFrontpageLayer is registered."""
        from collective.frontpage.interfaces import ICollectiveFrontpageLayer
        from plone.browserlayer import utils

        self.assertIn(ICollectiveFrontpageLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_FRONTPAGE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstallProducts(["collective.frontpage"])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.frontpage is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled("collective.frontpage"))

    def test_browserlayer_removed(self):
        """Test that ICollectiveFrontpageLayer is removed."""
        from collective.frontpage.interfaces import ICollectiveFrontpageLayer
        from plone.browserlayer import utils

        self.assertNotIn(ICollectiveFrontpageLayer, utils.registered_layers())
