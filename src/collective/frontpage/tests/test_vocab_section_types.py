# -*- coding: utf-8 -*-

from collective.frontpage import _
from collective.frontpage.testing import COLLECTIVE_FRONTPAGE_INTEGRATION_TESTING  # noqa: 501
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.interfaces import IVocabularyTokenized

import unittest


class SectionTypesIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_FRONTPAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_vocab_section_types(self):
        vocab_name = "collective.frontpage.SectionTypes"
        factory = getUtility(IVocabularyFactory, vocab_name)
        self.assertTrue(IVocabularyFactory.providedBy(factory))

        vocabulary = factory(self.portal)
        self.assertTrue(IVocabularyTokenized.providedBy(vocabulary))

        self.assertEqual(vocabulary.getTerm(u"welcome").title, _(u"Welcome Section"))
        self.assertEqual(vocabulary.getTerm(u"teaser").title, _(u"Teaser Section"))
        self.assertEqual(vocabulary.getTerm(u"static").title, _(u"Static Section"))
        self.assertEqual(vocabulary.getTerm(u"news").title, _(u"News Section"))
        self.assertEqual(vocabulary.getTerm(u"tiles").title, _(u"Tiles Section"))
        self.assertEqual(vocabulary.getTerm(u"search").title, _(u"Search Section"))
