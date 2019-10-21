# -*- coding: utf-8 -*-
from collective.frontpage.testing import COLLECTIVE_FRONTPAGE_FUNCTIONAL_TESTING  # noqa: 501
from collective.frontpage.testing import COLLECTIVE_FRONTPAGE_INTEGRATION_TESTING  # noqa: 501
from plone import api
from plone.app.testing import login, SITE_OWNER_PASSWORD
from plone.app.testing import logout
from plone.app.testing import setRoles
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import TEST_USER_ID
from plone.testing._z2_testbrowser import Browser

import transaction
import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_FRONTPAGE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.frontpage = api.content.create(
            self.portal, "Frontpage", "my-frontpage", "My Frontpage"
        )
        self.section = api.content.create(
            self.frontpage, "Teaser", "my-section", "My Teaser"
        )

    def test_frontpage_is_registered(self):
        view = self.section.restrictedTraverse("view")
        self.assertTrue(view(), "section is not found")
        self.assertTrue(
            "My Teaser" in view(), "Teaser Title is not found in the view"
        )


class ViewsFunctionalTest(unittest.TestCase):

    layer = COLLECTIVE_FRONTPAGE_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.browser = Browser(self.layer["app"])
        self.browser.handleErrors = False
        login(self.portal, SITE_OWNER_NAME)

    def test_redirects_on_anonymous(self):
        frontpage = api.content.create(
            container=self.portal,
            type='Frontpage',
            id='my-frontpage',
            title="Frontpage",
        )
        api.content.transition(obj=frontpage, transition='publish')
        search = self._create_and_publish(frontpage, 'Search')
        static = self._create_and_publish(frontpage, 'Static')
        news = self._create_and_publish(frontpage, 'News')
        teaser = self._create_and_publish(frontpage, 'Teaser')
        tiles = self._create_and_publish(frontpage, 'Tiles')

        item = api.content.create(
            container=tiles,
            type='Item',
            id='item',
            title='Item',
        )
        api.content.transition(obj=item, transition='publish')
        transaction.commit()

        self._login_with_browser()
        self.browser.open(item.absolute_url())
        self.assertEqual(self.browser.url, item.absolute_url() + '/edit')
        self._logout_with_browser()

        logout()
        for i in (search, static, teaser, news, tiles, item):
            self.browser.open(i.absolute_url())
            self.assertEqual(self.browser.url, frontpage.absolute_url())

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
