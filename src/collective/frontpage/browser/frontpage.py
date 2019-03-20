# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Frontpage(BrowserView):
    template = ViewPageTemplateFile('templates/frontpage.pt')

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        return self.template()

    def text_color(self):
        if self.context.background_image:
            return '#FFF'
        else:
            return self.contrasting_text_color(self.context.background_color)

    def button_text_color(self):
        return self.contrasting_text_color(self.context.primary_color)

    def contrasting_text_color(self, hex_str):
        '''
        Input a string without hash sign of RGB hex digits to compute
        complementary contrasting color such as for fonts
        '''

        hex_str = hex_str.replace('#', '')
        if len(hex_str) == 6:
            (r, g, b) = (hex_str[:2], hex_str[2:4], hex_str[4:])
        elif len(hex_str) == 8:
            (r, g, b) = (hex_str[2:4], hex_str[4:6], hex_str[6:])
        elif len(hex_str) == 3:
            (r, g, b) = (hex_str[:1], hex_str[1:2], hex_str[2:])
        else:
            return '#000'
        return '#000' if 1 - (int(r, 16) * 0.299 + int(g, 16) * 0.587 + int(b, 16) * 0.114) / 255 < 0.5 else '#fff'  # noqa
