# -*- coding: utf-8 -*-
from collective.frontpage import _
from collective.frontpage.testing import (
    COLLECTIVE_FRONTPAGE_INTEGRATION_TESTING,
)  # noqa: 501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.interfaces import IVocabularyTokenized

import unittest


class SectionBackgroundColorsIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_FRONTPAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_vocab_section_background_colors(self):

        section_colors = api.portal.get_registry_record(
            "collective.frontpage.section_colors"
        )
        self.assertIn(u"None | rgba(0,0,0,0)", section_colors)
        self.assertIn(u"Plone Blue | #0083BE", section_colors)
        self.assertIn(u"Dirty White | #F5F5F5", section_colors)

        vocab_name = "collective.frontpage.SectionColors"
        factory = getUtility(IVocabularyFactory, vocab_name)
        self.assertTrue(IVocabularyFactory.providedBy(factory))
        vocabulary = factory(self.portal)
        self.assertTrue(IVocabularyTokenized.providedBy(vocabulary))
        self.assertEqual(vocabulary.getTerm(u"rgba(0,0,0,0)").title, _(u"None"))
        self.assertEqual(vocabulary.getTerm(u"#0083BE").title, _(u"Plone Blue"))
        self.assertEqual(vocabulary.getTerm(u"#F5F5F5").title, _(u"Dirty White"))

    def test_edge_case_names_not_crashing_vocab(self):
        faulty_list = [
            u"Normal Value | rgba(0,0,0,1)",
            u"Normal Value | rgba(0,0,0,1)",
            u"Pipe is missing here",
            u"T¡m€ to ¹ | rgba(0,0,0,2)",
            u"Wasted | rgba(¹,²,³, ¼)",
        ]
        api.portal.set_registry_record(
            "collective.frontpage.section_colors", faulty_list
        )

        vocab_name = "collective.frontpage.SectionColors"
        factory = getUtility(IVocabularyFactory, vocab_name)
        self.assertTrue(IVocabularyFactory.providedBy(factory))
        vocabulary = factory(self.portal)
        self.assertTrue(IVocabularyTokenized.providedBy(vocabulary))
        self.assertIn(u"rgba(0,0,0,1)", vocabulary)
        self.assertIn(u"rgba(0,0,0,2)", vocabulary)
        self.assertEqual(2, len(vocabulary))
