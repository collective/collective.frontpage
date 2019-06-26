# -*- coding: utf-8 -*-

from collective.frontpage.browser.mixins import SectionViewMixin
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class SectionView(SectionViewMixin, BrowserView):

    template = ViewPageTemplateFile('templates/section.pt')

    def __call__(self):
        self.layout = self.context.getLayout()
        self.contents = self.context.listFolderContents()
        return self.template()

    def is_layout(self, layout):
        if layout == self.layout:
            return True
        return False
