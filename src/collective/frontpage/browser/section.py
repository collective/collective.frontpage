# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class SectionView(BrowserView):

    template = ViewPageTemplateFile('templates/section.pt')

    def __call__(self):
        return self.template()

    def set_color(self):
        return 'color: {0}'.format(self.context.background_color)
