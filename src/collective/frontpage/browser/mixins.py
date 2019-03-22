# -*- coding: utf-8 -*-

import ast


class SectionViewMixin():

    def text_color(self, section):
        if section.background_image:
            return '#FFF'
        else:
            return self.contrasting_text_color(section.background_color)

    def button_text_color(self, section):
        return self.contrasting_text_color(section.primary_color)

    def contrasting_text_color(self, hex_val):
        '''
        Input a string without hash sign of RGB hex digits to compute
        complementary contrasting color such as for fonts
        '''
        alpha = 1
        r, g, b = ('255', '255', '255')

        if '#' in hex_val:
            hex_val = hex_val.replace('#', '')

            if len(hex_val) == 6:
                (r, g, b) = (hex_val[:2], hex_val[2:4], hex_val[4:])
            elif len(hex_val) == 3:
                (r, g, b) = (hex_val[:1], hex_val[1:2], hex_val[2:])

        if 'rgba' in hex_val:
            value = hex_val.replace('rgba', '').strip()
            r, g, b, alpha = ast.literal_eval(value)

        if 'rgb' in hex_val:
            value = hex_val.replace('rgb', '').strip()
            r, g, b = ast.literal_eval(value)

        for key in ['r', 'g', 'b']:
            local_val = getattr(self, key)
            if isinstance(local_val, int):
                local_val = str(local_val)

        return '#000' if 1 - (int(r, 16) * 0.299 + int(g, 16) * 0.587 + int(b, 16) * 0.114) / 255 < 0.5 else '#FFF'  # noqa: 501
