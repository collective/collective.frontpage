# -*- coding: utf-8 -*-
from collective.frontpage.testing import COLLECTIVE_FRONTPAGE_FUNCTIONAL_TESTING  # noqa: 501
from plone import api
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.app.testing import TEST_USER_ID
from plone.testing._z2_testbrowser import Browser

import transaction
import unittest


class ViewsFunctionalTest(unittest.TestCase):

    layer = COLLECTIVE_FRONTPAGE_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.browser = Browser(self.layer["app"])
        self.browser.handleErrors = False
        login(self.portal, SITE_OWNER_NAME)

    def test_frontpage_is_registered(self):
        # This used to be an integration test. However since we use zcml conditions to
        # use different layouts for tokyo and not tokyo
        # the integration tests think that tokyo is installed while it is not.
        # Thus the content is put into a fill-slot "fluid" which is not available
        # without tokyo really installed.
        # As a workaround we really install tokyo now. If there is more time, please
        # feel free to fix the integration test!
        frontpage = api.content.create(
            self.portal, "Frontpage", "my-frontpage", "My Frontpage"
        )
        teaser = api.content.create(frontpage, "Teaser", "my-section", "My Teaser")
        api.content.transition(obj=frontpage, transition='publish')
        api.content.transition(obj=teaser, transition='publish')
        transaction.commit()
        self._install_tokyo()
        self._login_with_browser()
        self.browser.open(frontpage.absolute_url())
        self.assertIn('My Teaser', self.browser.contents)

    def test_frontpage_fill_slot(self):
        frontpage = api.content.create(
            container=self.portal,
            type='Frontpage',
            id='my-frontpage',
            title="Frontpage",
        )
        api.content.transition(obj=frontpage, transition='publish')
        self._create_and_publish(frontpage, 'Static')
        transaction.commit()
        self._login_with_browser()

        # Without Tokyo it should be fill-slot main:
        self.browser.open(frontpage.absolute_url())
        self.assertIn('<divclass="container">\n<divclass="row">\n<asideid', self.browser.contents.replace(' ', ''))  # noqa
        self.assertNotIn('<divid="content', self.browser.contents)

        self._install_tokyo()

        self.assertTrue(self.installer.isProductInstalled("collective.frontpage"))
        self.assertTrue(self.installer.isProductInstalled("plonetheme.tokyo"))

        self.browser.open(frontpage.absolute_url())
        self.assertIn('<divid="content">\n\n\n\n\n\n\n\n\n\n\n\n<divclass="editable-section"', self.browser.contents.replace(' ', ''))  # noqa
        self.assertNotIn('<divclass="container"', self.browser.contents)

    def _install_tokyo(self):
        # With Tokyo it should be fill-slot fluid
        from Testing.ZopeTestCase import installProduct
        installProduct(self.portal.getPhysicalRoot(), 'collective.sidebar')
        installProduct(self.portal.getPhysicalRoot(), 'plonetheme.tokyo')
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.installProduct('plonetheme.tokyo')
        transaction.commit()

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
