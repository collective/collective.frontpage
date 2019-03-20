# -*- coding: utf-8 -*-

from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class IFrontpage(model.Schema):
    """
    Marker interface and Dexterity Python Schema for Frontpage.
    """

    pass


@implementer(IFrontpage)
class Frontpage(Container):

    pass
