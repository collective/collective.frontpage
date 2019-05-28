# -*- coding: utf-8 -*-

from collective.frontpage import _
from collective.frontpage.testing import (
    COLLECTIVE_FRONTPAGE_INTEGRATION_TESTING,
)  # noqa: 501
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

        # VocabItem(u'welcome', _(u'Welcome Section')),
        # VocabItem(u'teaser', _(u'Teaser Section')),
        # VocabItem(u'static', _(u'Static Section')),
        # VocabItem(u'news', _(u'News Section')),
        # VocabItem(u'tiles', _(u'Tiles Section')),
        # VocabItem(u'search', _(u'Search Section')),

        self.assertEqual(vocabulary.getTerm(u"welcome").title, _(u"Welcome Section"))
