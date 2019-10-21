# -*- coding: utf-8 -*-

from collective.frontpage.browser.mixins import SectionsViewMixin
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class TilesBase(SectionsViewMixin, BrowserView):
    """TilesBase base class"""


class TilesCardView(TilesBase):
    """TilesCardView base class"""

    template = ViewPageTemplateFile("templates/sections/tile_cards.pt")


class TilesCascadeView(TilesBase):
    """TilesCascadeView base class"""

    template = ViewPageTemplateFile("templates/sections/tile_cascade.pt")
