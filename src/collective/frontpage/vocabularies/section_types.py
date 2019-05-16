# -*- coding: utf-8 -*-

from collective.frontpage import _
from plone.dexterity.interfaces import IDexterityContent
from zope.globalrequest import getRequest
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class VocabItem(object):
    def __init__(self, token, value):
        self.token = token
        self.value = value


@implementer(IVocabularyFactory)
class SectionTypes(object):

    def __call__(self, context):
        items = [
            VocabItem(u'welcome', _(u'Welcome Section')),
            VocabItem(u'teaser', _(u'Teaser Section')),
            VocabItem(u'static', _(u'Static Section')),
            VocabItem(u'news', _(u'News Section')),
            VocabItem(u'tiles', _(u'Tiles Section')),
            VocabItem(u'search', _(u'Search Section')),
        ]

        # Fix context if you are using the vocabulary in DataGridField.
        # See https://github.com/collective/collective.z3cform.datagridfield/issues/31:  # noqa: 501
        if not IDexterityContent.providedBy(context):
            req = getRequest()
            context = req.PARENTS[0]

        # Create a list of SimpleTerm items:
        terms = []
        for item in items:
            terms.append(
                SimpleTerm(
                    value=item.token,
                    token=str(item.token),
                    title=item.value,
                )
            )
        # Create a SimpleVocabulary from the terms list and return it:
        return SimpleVocabulary(terms)


SectionTypesFactory = SectionTypes()
