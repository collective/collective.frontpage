# -*- coding: utf-8 -*-

from collective.frontpage.browser.mixins import SectionsViewMixin
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from BeautifulSoup import BeautifulSoup
import re


class Frontpage(SectionsViewMixin, BrowserView):

    template = ViewPageTemplateFile("templates/frontpage.pt")

    def __call__(self):
        return self.template()

    def _render_sections(self):
        contents = self.context.listFolderContents()
        output = str()
        for section in contents:
            parsed_html = BeautifulSoup(section())
            output += str(
                parsed_html.body.find(
                    'div', attrs={'class': re.compile('^frontpage-section*')}
                )
            )
        return output
