# -*- coding: utf-8 -*-

from collective.frontpage.browser.mixins import SectionViewMixin
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Frontpage(SectionViewMixin, BrowserView):
    template = ViewPageTemplateFile('templates/frontpage.pt')

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        return self.template()
