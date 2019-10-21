# -*- coding: utf-8 -*-

from lxml import html
from plone import api
from plone.memoize.view import memoize
from Products.Five.browser import BrowserView


class Frontpage(BrowserView):

    section_classname = 'frontpage-section'

    def is_anonymous(self):
        return api.user.is_anonymous()

    @memoize
    def get_sections(self):
        contents = self.context.listFolderContents()
        section_list = list()
        for section in contents:
            section_url = section.absolute_url()
            section_view = section.unrestrictedTraverse(section.getLayout())
            section_view.request.set('from_fp', True)
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
