# -*- coding: utf-8 -*-

from plone.dexterity.content import Container
from plone.supermodel import model


class ISearch(model.Schema):
    """
    Marker interface and Dexterity Python Schema for Search.
    """

    pass


class Search(Container):

    pass
