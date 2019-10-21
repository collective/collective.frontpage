# -*- coding: utf-8 -*-
from collective.frontpage.testing import COLLECTIVE_FRONTPAGE_INTEGRATION_TESTING  # noqa: 501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


class NewsViewIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_FRONTPAGE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.frontpage = api.content.create(
            self.portal, "Frontpage", "my-frontpage", "My Frontpage"
        )
        self.section = api.content.create(
            self.frontpage, "News", "my-section", "My News"
        )

    def test_news_section_is_registered(self):
        view = self.section.restrictedTraverse("view")
        self.assertTrue(view(), "section is not found")
        self.assertTrue("My News" in view(), "News Title is not found in the view")

    def test_get_news(self):
        self.news_item = api.content.create(
            self.portal, "News Item", "my-news", "My News Item",
            Date="2219-10-21T08:56:30+00:00"
        )
        view = self.section.restrictedTraverse("news_default")
        # should be 3 because of the 3 in demo profile:
        self.assertTrue(len(view.get_news()) == 3, "News Item not found")
        self.assertTrue("My News Item" in view(), "News Item not found in the view")
