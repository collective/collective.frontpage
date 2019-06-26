# -*- coding: utf-8 -*-

from plone.dexterity.content import Container
from plone.supermodel import model


class ITeaser(model.Schema):
    """
    Marker interface and Dexterity Python Schema for Teaser.
    """

    pass


class Teaser(Container):

    pass
