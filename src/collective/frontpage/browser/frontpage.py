# -*- coding: utf-8 -*-

from lxml import html
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api


class Frontpage(BrowserView):

    template = ViewPageTemplateFile("templates/frontpage.pt")

    def __call__(self):
        self.section_classname = 'frontpage-section'
        return self.template()

    def is_anonymous(self):
        return api.user.is_anonymous()

    def get_sections(self):
        contents = self.context.listFolderContents()
        section_list = list()
        for section in contents:
            section_url = section.absolute_url()
            section_view = section.unrestrictedTraverse(section.getLayout())
            section_view.request.set('ajax_load', 'True')
            tree = html.fromstring(section_view())
            parsed_html = tree.xpath(
                '//div[contains(@class, "{0}")]'.format(
                    self.section_classname
                )
            )
            for elem in parsed_html:
                section_list.append(
                    {
                        'url': section_url,
                        'html': html.tostring(elem),
                        'style': section_view.get_style(),
                    }
                )
        return section_list
