# -*- coding: utf-8 -*-

from collective.frontpage import _
from plone.dexterity.content import Item
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from zope import schema


class IItem(model.Schema):
    """
    Marker interface and Dexterity Python Schema for Item.
    """

    icon = schema.TextLine(
        title=_(u'item_contenttype_icon_title_icon', default=u'Icon'),
        description=_(
            u'item_contenttype_icon_description_icon',
            default=u'Select an available icon.'),
        required=False,
    )

    image = NamedBlobImage(
        title=_(u'item_contenttype_image_title_icon', default=u'Image'),
        required=False,
    )


class Item(Item):

    pass
