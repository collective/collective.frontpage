# -*- coding: utf-8 -*-

from collective.frontpage import _
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Frontpage(BrowserView):
    template = ViewPageTemplateFile('templates/frontpage.pt')

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        self.msg = _(u'A small message')
        return self.template()
