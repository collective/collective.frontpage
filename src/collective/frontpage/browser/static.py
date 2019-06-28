# -*- coding: utf-8 -*-

from collective.frontpage.browser.mixins import SectionsViewMixin
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class StaticBase(SectionsViewMixin, BrowserView):
    """StaticBase base class"""


class StaticDefaultView(StaticBase):
    """StaticDefaultView base class"""

    template = ViewPageTemplateFile("templates/sections/static_default.pt")

    def __call__(self):
        return self.template()
