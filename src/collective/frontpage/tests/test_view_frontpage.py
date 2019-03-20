# -*- coding: utf-8 -*-

from collective.frontpage.testing import COLLECTIVE_FRONTPAGE_FUNCTIONAL_TESTING  # noqa: 501
from collective.frontpage.testing import COLLECTIVE_FRONTPAGE_INTEGRATION_TESTING  # noqa: 501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getMultiAdapter

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_FRONTPAGE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(self.portal, 'Frontpage', 'my-frontpage')

    def test_frontpage_is_registered(self):
        view = getMultiAdapter(
            (self.portal['my-frontpage'], self.portal.REQUEST),
            name='view'
        )
        self.assertTrue(view(), 'frontpage is not found')
        self.assertTrue(
            'Sample View' in view(),
            'Sample View is not found in frontpage'
        )
        self.assertTrue(
            'Sample View' in view(),
            'A small message is not found in frontpage'
        )


class ViewsFunctionalTest(unittest.TestCase):

    layer = COLLECTIVE_FRONTPAGE_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
