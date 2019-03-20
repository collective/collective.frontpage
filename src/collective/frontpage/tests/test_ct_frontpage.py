# -*- coding: utf-8 -*-

from collective.frontpage.content.frontpage import IFrontpage  # noqa: 501
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


class FrontpageIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_FRONTPAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_ct_frontpage_schema(self):
        fti = queryUtility(IDexterityFTI, name='Frontpage')
        schema = fti.lookupSchema()
        self.assertEqual(IFrontpage, schema)

    def test_ct_frontpage_fti(self):
        fti = queryUtility(IDexterityFTI, name='Frontpage')
        self.assertTrue(fti)

    def test_ct_frontpage_factory(self):
        fti = queryUtility(IDexterityFTI, name='Frontpage')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IFrontpage.providedBy(obj),
            u'IFrontpage not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_frontpage_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Frontpage',
            id='frontpage',
        )

        self.assertTrue(
            IFrontpage.providedBy(obj),
            u'IFrontpage not provided by {0}!'.format(
                obj.id,
            ),
        )

    def test_ct_frontpage_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Frontpage')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_frontpage_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Frontpage')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'frontpage_id',
            title='Frontpage container',
        )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
