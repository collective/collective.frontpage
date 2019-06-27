# -*- coding: utf-8 -*-

from collective.frontpage.content.item import IItem
from collective.frontpage.testing import COLLECTIVE_FRONTPAGE_INTEGRATION_TESTING  # noqa: 501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


try:
    from plone.dexterity.schema import portalTypeToSchemaName
except ImportError:
    # Plone < 5
    from plone.dexterity.utils import portalTypeToSchemaName  # noqa: F401


class ItemIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_FRONTPAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            "Teaser", self.portal, "item", title="Parent container"
        )
        self.parent = self.portal[parent_id]

    def test_ct_item_schema(self):
        fti = queryUtility(IDexterityFTI, name="Item")
        schema = fti.lookupSchema()
        self.assertEqual(IItem, schema)

    def test_ct_item_fti(self):
        fti = queryUtility(IDexterityFTI, name="Item")
        self.assertTrue(fti)

    def test_ct_item_factory(self):
        fti = queryUtility(IDexterityFTI, name="Item")
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IItem.providedBy(obj), u"IItem not provided by {0}!".format(obj)
        )

    def test_ct_item_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(container=self.parent, type="Item", id="item")

        self.assertTrue(
            IItem.providedBy(obj), u"IItem not provided by {0}!".format(obj.id)
        )

    def test_ct_item_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Item")
        self.assertFalse(fti.global_allow, u"{0} is globally addable!".format(fti.id))
