# -*- coding: utf-8 -*-

from collective.frontpage.testing import COLLECTIVE_FRONTPAGE_FUNCTIONAL_TESTING  # noqa: 501
from collective.frontpage.testing import COLLECTIVE_FRONTPAGE_INTEGRATION_TESTING  # noqa: 501
from plone import api
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.app.testing import TEST_USER_ID
from plone.testing._z2_testbrowser import Browser
from plone.testing.zope import installProduct
from zope.component import getMultiAdapter

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_FRONTPAGE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        frontpage = api.content.create(
            self.portal, "Frontpage", "my-frontpage", "My Frontpage"
        )
        api.content.create(frontpage, "Teaser", "my-section", "My Teaser")

    def test_frontpage_is_registered(self):
        view = getMultiAdapter(
            (self.portal["my-frontpage"], self.portal.REQUEST), name="view"
        )
        self.assertTrue(view(), "frontpage is not found")
        self.assertTrue(
            "My Teaser" in view(), "Teaser Title is not found in frontpage"
        )


class ViewsFunctionalTest(unittest.TestCase):

    layer = COLLECTIVE_FRONTPAGE_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.browser = Browser(self.layer["app"])
        self.browser.handleErrors = False
        login(self.portal, SITE_OWNER_NAME)

    def test_frontpage_fill_slot(self):
        frontpage = api.content.create(
            container=self.portal,
            type='Frontpage',
            id='my-frontpage',
            title="Frontpage",
        )
        api.content.transition(obj=frontpage, transition='publish')
        self._login_with_browser()

        # Without Tokyo it should be fill-slot main:
        self.browser.open(frontpage.absolute_url())
        self.assertIn('<divid="content"><divclass="content-innercontainer">', self.browser.contents.replace(' ', ''))  # noqa

        # With Tokyo it should be fill-slot fluid
        installProduct(self.layer["app"], 'collective.sidebar')
        installProduct(self.layer["app"], 'plonetheme.tokyo')
        self.browser.open(frontpage.absolute_url())
        self.assertIn('<divid="content"><divclass="editable-section">', self.browser.contents.replace(' ', ''))  # noqa



    def _login_with_browser(self):
        self.browser.open(self.portal.absolute_url() + "/login_form")
        self.browser.getControl(name='__ac_name').value = SITE_OWNER_NAME
        self.browser.getControl(name='__ac_password').value = SITE_OWNER_PASSWORD
        self.browser.getControl(name='submit').click()

    def _logout_with_browser(self):
        self.browser.open(self.portal.absolute_url() + '/' + 'logout')

    @staticmethod
    def _create_and_publish(frontpage, type):
        section = api.content.create(
            container=frontpage,
            type=type,
            id=type.lower(),
            title=type,
        )
        api.content.transition(obj=section, transition='publish')
        return section
