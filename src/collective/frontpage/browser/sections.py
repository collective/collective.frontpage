# -*- coding: utf-8 -*-

from collective.frontpage.browser.mixins import SectionsViewMixin
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api


class SectionsView(SectionsViewMixin, BrowserView):

    template = ViewPageTemplateFile('templates/sections.pt')

    def __call__(self):
        self.layout = self.context.getLayout()
        self.contents = self.context.listFolderContents()
        self.portal = api.portal.get()
        return self.template()

    def get_portal_url(self):
        return self.portal.absolute_url()

    def get_style(self):
        bg_image = 'background-image:url({0}/@@images/background_image)'.format(  # noqa: 501
            self.context.absolute_url()
        )
        bg_color = 'background-color:{0}'.format(
            self.context.background_color
        )
        text_color = 'color:{0}'.format(
            self.text_color(self.context)
        )
        return (bg_image if self.context.background_image else bg_color) + ';' + text_color  # noqa: 501

    def is_layout(self, layout):
        if layout == self.layout:
            return True
        return False
