# -*- coding: utf-8 -*-

from collective.frontpage.browser.mixins import SectionsViewMixin
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class TeaserBase(SectionsViewMixin, BrowserView):
    """TeaserBase base class"""


class TeaserDefaultView(TeaserBase):
    """TeaserDefaultView base class"""

    template = ViewPageTemplateFile("templates/sections/teaser_default.pt")

    def __call__(self):
        return self.template()
