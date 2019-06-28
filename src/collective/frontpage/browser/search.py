# -*- coding: utf-8 -*-

from collective.frontpage.browser.mixins import SectionsViewMixin
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api


class SearchBase(SectionsViewMixin, BrowserView):
    """SearchBase base class"""


class SearchBarView(SearchBase):
    """SearchBarView base class"""

    template = ViewPageTemplateFile("templates/sections/search_bar.pt")

    def __call__(self):
        self.portal = api.portal.get()
        return self.template()
