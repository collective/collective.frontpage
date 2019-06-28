# -*- coding: utf-8 -*-

from plone.dexterity.content import Container
from plone.supermodel import model


class ITiles(model.Schema):
    """
    Marker interface and Dexterity Python Schema for Tiles.
    """

    pass


class Tiles(Container):

    pass
