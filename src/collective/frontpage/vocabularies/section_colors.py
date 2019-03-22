# -*- coding: utf-8 -*-

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
        # TODO: Get from colors and list_to_dict()  # noqa: T000
        # ldap_objectclass_mapping = api.portal.get_registry_record(
        #   name='operun.crm.ldap_objectclass_mapping')

        items = [
            VocabItem(u'#0083BE', u'Plone Blue',),
            VocabItem(u'#F5F5F5', u'Dirty White'),
            VocabItem(u'rgba(0,0,0,1)', u'None'),
            VocabItem(u'rgb(255,0,0)', u'Red'),
            VocabItem(u'rgba(0,0,0,0.5)', u'Semi Transparent'),
            VocabItem(u'rgba(255,0,0,0.5)', u'Red Transparent'),
            VocabItem(u'rgb(25,25,112)', u'Dark Blue RGB'),
            VocabItem(u'rgb(173,255,47)', u'Light Green RGB'),
        ]

        # Fix context if you are using the vocabulary in DataGridField.
        # See https://github.com/collective/collective.z3cform.datagridfield/issues/31:  # noqa: 501
        if not IDexterityContent.providedBy(context):
            req = getRequest()
            context = req.PARENTS[0]

        # create a list of SimpleTerm items:
        terms = []
        for item in items:
            terms.append(
                SimpleTerm(
                    value=item.token,
                    token=str(item.token),
                    title=item.value,
                )
            )

        return SimpleVocabulary(terms)

    def list_to_dict(self, list_of_items):
        """
        Converts list mappings into dict.
        """
        return dict(item.split('|') for item in list_of_items)


SectionColorsFactory = SectionColors()
