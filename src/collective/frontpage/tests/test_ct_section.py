# -*- coding: utf-8 -*-

from collective.frontpage.content.section import ISection
from collective.frontpage.testing import COLLECTIVE_FRONTPAGE_INTEGRATION_TESTING  # noqa: 501
from plone import api
from plone.api.exc import InvalidParameterError
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


class SectionIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_FRONTPAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            "Frontpage", self.portal, "section", title="Parent container"
        )
        self.parent = self.portal[parent_id]

    def test_ct_section_schema(self):
        fti = queryUtility(IDexterityFTI, name="Section")
        schema = fti.lookupSchema()
        self.assertEqual(ISection, schema)

    def test_ct_section_fti(self):
        fti = queryUtility(IDexterityFTI, name="Section")
        self.assertTrue(fti)

    def test_ct_section_factory(self):
        fti = queryUtility(IDexterityFTI, name="Section")
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ISection.providedBy(obj), u"ISection not provided by {0}!".format(obj)
        )

    def test_ct_section_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(container=self.parent, type="Section", id="section")

        self.assertTrue(
            ISection.providedBy(obj), u"ISection not provided by {0}!".format(obj.id)
        )

    def test_ct_section_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Section")
        self.assertFalse(fti.global_allow, u"{0} is globally addable!".format(fti.id))

    def test_ct_section_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Section")
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id, self.portal, "section_id", title="Section container"
        )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent, type="Document", title="My Content"
            )
