# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model


class INews(model.Schema):
    """
    Marker interface and Dexterity Python Schema for Static.
    """

    pass


class News(Container):

    pass
