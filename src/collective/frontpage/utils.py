# -*- coding: utf-8 -*-

from collective.frontpage import _
from plone import api
from zope.i18n import translate


def get_translated(text, context, domain="plone", multi_domain=False):
    """
    Useful for multi-domain translations.
    e.g. Fetching Plone default translations.
    """
    if context:
        request = context.REQUEST
        language_id = request.response.headers.get("content-language", None)
        if language_id:
            translated = translate(text, domain=domain, target_language=language_id)  # noqa: 501
            if multi_domain:
                if translated != text:
                    return translated
                package_domain = _._domain
                package_translated = translate(
                    text, domain=package_domain, target_language=language_id
                )
                if package_translated != text:
                    return package_translated
            return translated
    return text


def crop(text, max_char_length):
    """
    Crop given text by full words to given count of chars.
    """
    if len(text) > max_char_length:
        cleared_text = text
        special_chars = [u'.', u',', u':', u';']
        for s in special_chars:
            cleared_text = cleared_text.replace(s, u' ')
        cropped_text = u' '.join((cleared_text[0:max_char_length].strip()).split(u' ')[:-1])  # noqa
        if len(cropped_text) == 0:
            cropped_text = cleared_text[0:max_char_length].strip()
        return cropped_text + u'...'
    return text


def get_user():
    """
    Return MemberData, ID and profile directory for the current user.
    """
    user = api.user.get_current()
    user_id = user.id
    user_dir = "/users/{0}".format(user_id)
    return user, user_id, user_dir
