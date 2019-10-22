# -*- coding: utf-8 -*-

from collective.frontpage.browser.mixins import SectionsViewMixin
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class SearchBase(SectionsViewMixin, BrowserView):
    """SearchBase base class"""


class MinimalSearchBarView(SearchBase):

    template = ViewPageTemplateFile("templates/sections/search_minimal.pt")


class DefaultSearchView(SearchBase):

    template = ViewPageTemplateFile('templates/sections/search_default.pt')
