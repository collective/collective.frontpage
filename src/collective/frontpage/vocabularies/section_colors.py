# -*- coding: utf-8 -*-

from plone import api
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

import logging


logger = logging.getLogger("collective.frontpage")


class VocabItem(object):
    def __init__(self, token, value):
        self.token = token
        self.value = value

    def __str__(self):
        return '<Color {0}: {1}>'.format(self.value, self.token)

    __repr__ = __str__


@implementer(IVocabularyFactory)
class SectionColors(object):
    def __call__(self, context):
        items = self._get_colors_from_registry()
        terms = self._create_simple_terms(items)
        voc = self._create_vocabulary(terms)
        return voc

    @staticmethod
    def _get_colors_from_registry():
        """Get colors and list_to_dict()"""
        items = list()
        section_colors = api.portal.get_registry_record(
            "collective.frontpage.section_colors"
        )
        for color in section_colors:
            try:
                split = color.split("|")
                items.append(VocabItem(split[1].strip(), split[0].strip()))
            except IndexError:
                logger.exception(
                    "Could not use color {color} -> Please check the settings to make "
                    "your custom color available! "
                    "Each line should contain a Pipe Symbol".format(color=color)
                )
        return items

    @staticmethod
    def _create_simple_terms(items):
        """Create a list of SimpleTerm items"""
        terms = []
        for item in items:
            try:
                if item:
                    if item.token in [x.value for x in terms]:
                        try:
                            logger.warning(
                                "Could not add {color} ({color_hex}), "
                                "because it is already defined "
                                "as {duplicate}({duplicate_hex}).".format(
                                    color=item.value,
                                    duplicate=x.title,
                                    color_hex=item.token,
                                    duplicate_hex=x.token
                                )
                            )
                        except():
                            logger.warning("Could not add {color}".format(color=item.value))  # noqa
                    else:
                        term = SimpleTerm(
                            value=item.token, token=str(item.token), title=item.value
                        )
                        terms.append(term)
            except UnicodeEncodeError:
                logger.exception(
                    "Could not use one of your custom colors -> Please check the "
                    "settings to make your custom color available! "
                    "Please don't use special characters in RGB-Values!"
                )
        return terms

    @staticmethod
    def _create_vocabulary(terms):
        return SimpleVocabulary(terms, swallow_duplicates=True)

    @staticmethod
    def list_to_dict(list_of_items):
        """Converts list mappings into dict"""
        try:
            return dict(item.split("|") for item in list_of_items)
        except ValueError:
            return dict()


SectionColorsFactory = SectionColors()
