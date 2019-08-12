# -*- coding: utf-8 -*-
from collective.frontpage.browser.mixins import SectionsViewMixin
from collective.frontpage.utils import crop
from plone import api
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class NewsBase(SectionsViewMixin, BrowserView):
    """TeaserBase base class"""

    def get_news(self):
        results = []
        items = api.content.find(
            portal_type='News Item',
            sort_on='Date',
            sort_order='descending',
            Language=api.portal.get_current_language(),
        )
        if items:
            items = [item.getObject() for item in items]
            for item in items:
                title = item.title
                description = crop(item.description, 200)
                url = item.absolute_url()
                scaled_image = None
                if item.image:
                    images_view = api.content.get_view(
                        'images', item, self.request)
                    scaled_image = images_view.scale(
                        'image', width=640, height=420, direction='down')
                data = {
                    'title': title,
                    'description': description,
                    'url': url,
                    'scaled_image': scaled_image,
                }
                results.append(data)
        return results[:3]


class NewsDefaultView(NewsBase):
    """TeaserDefaultView base class"""

    template = ViewPageTemplateFile("templates/sections/news_default.pt")
