# -*- coding: utf-8 -*-

from plone.app.textfield import RichText
from plone.dexterity.content import Item
from plone.supermodel import model
from zope import schema
from zope.interface import implementer
from plone.namedfile.field import NamedBlobImage
from collective.frontpage import _


class IItem(model.Schema):
    """
    Marker interface and Dexterity Python Schema for Item.
    """

    link_url = schema.URI(
        title=_(u'Link'),
        required=False,
    )

    link_title = schema.TextLine(
        title=_(u'Linktitle'),
        required=False,
    )

    icon = schema.TextLine(
        title=_(u'tile_icon_title', default='Icon'),
        description=_(u'tile_icon_description',
                      default=u'Select an available icon.'),
        required=False,
    )

    image = NamedBlobImage(
        title=_(u'Image'),
        required=False,
    )


class Item(Item):

    pass
