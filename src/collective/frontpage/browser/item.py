# -*- coding: utf-8 -*-
from plone import api
from Products.Five.browser import BrowserView


class ItemView(BrowserView):

    def __call__(self):
        if api.user.is_anonymous():
            parent = self.context.aq_parent.absolute_url()
            self.request.response.redirect(parent)
        else:
            self.request.response.redirect(self.context.absolute_url() + '/edit')
