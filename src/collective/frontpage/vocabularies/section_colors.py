# -*- coding: utf-8 -*-

from plone import api
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
class SectionColors(object):
    def __call__(self, context):
        # NOTE: Get colors and list_to_dict()
        items = list()
        section_colors = api.portal.get_registry_record(
            "collective.frontpage.section_colors"
        )
        for color in section_colors:
            split = color.split("|")
            items.append(VocabItem(split[1].strip(), split[0].strip()))
        # Fix context if you are using the vocabulary in DataGridField.
        # https://github.com/
        #   collective/collective.z3cform.datagridfield/issues/31
        if not IDexterityContent.providedBy(context):
            req = getRequest()
            context = req.PARENTS[0]
        # Create a list of SimpleTerm items
        terms = []
        for item in items:
            terms.append(
                SimpleTerm(value=item.token, token=str(item.token), title=item.value)
            )

        return SimpleVocabulary(terms)

    def list_to_dict(self, list_of_items):
        """Converts list mappings into dict"""
        return dict(item.split("|") for item in list_of_items)


SectionColorsFactory = SectionColors()
