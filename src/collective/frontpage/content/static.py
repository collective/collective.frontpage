# -*- coding: utf-8 -*-

from plone.dexterity.content import Container
from plone.supermodel import model


class IStatic(model.Schema):
    """
    Marker interface and Dexterity Python Schema for Static.
    """

    pass


class Static(Container):

    pass
