# -*- coding: utf-8 -*-

import ast


class SectionViewMixin(object):
    def text_color(self, section):
        if section.background_image:
            return "#FFF"
        else:
            return self._contrasting_text_color(section.background_color)

    def button_text_color(self, section):
        return self._contrasting_text_color(section.primary_color)

    @staticmethod
    def _contrasting_text_color(value):
        """
        Input a string with hash sign of RGB hex digits or rgb(1,2,3) or rgba(1,2,3,0.5)
        to compute complementary contrasting color such as for fonts
        """
        alpha = 1
        r, g, b = ("255", "255", "255")

        if "#" in value:
            value = value.replace("#", "")
            if len(value) == 3:
                value = u"".join(2 * s for s in value)
            if len(value) == 6:
                r, g, b = (value[:2], value[2:4], value[4:])

        elif "rgba" in value:
            value = value.replace("rgba", "").strip()
            r, g, b, alpha = ast.literal_eval(value)

        elif "rgb" in value:
            value = value.replace("rgb", "").strip()
            r, g, b = ast.literal_eval(value)

        r, g, b, alpha = [str(i) for i in (r, g, b, alpha)]

        return (
            "#000"
            if 1 - (int(r, 16) * 0.299 + int(g, 16) * 0.587 + int(b, 16) * 0.114) / 255
            < 0.5
            else "#FFF"
        )
