# -*- coding: utf-8 -*-

# from plone import api
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
class SectionBackgroundColors(object):
    """
    """

    def __call__(self, context):
        # TODO: Get from colors and list_to_dict()
        # ldap_objectclass_mapping = api.portal.get_registry_record(
        #   name='operun.crm.ldap_objectclass_mapping')  # noqa

        items = [
            VocabItem(u'#0083BE', u'Plone Blue',),
            VocabItem(u'#F5F5F5', u'Dirty White'),
        ]

        # Fix context if you are using the vocabulary in DataGridField.
        # See https://github.com/collective/collective.z3cform.datagridfield/issues/31:  # NOQA: 501
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

SectionBackgroundColorsFactory = SectionBackgroundColors()
