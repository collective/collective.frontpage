# -*- coding: utf-8 -*-

from collective.frontpage import _
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from zope import schema


class ISection(model.Schema):
    """
    Marker interface and Dexterity Python Schema for Section
    """

    section_type = schema.Choice(
        title=_(u"Type"),
        description=_(u"This changes the styling and content of the section."),
        default="static",
        vocabulary="collective.frontpage.SectionTypes",
        required=True,
    )

    background_color = schema.Choice(
        title=_(u"Background Color"),
        description=_(
            u"The Background-Color will always be on top of the "
            u"background-image. Make sure to use transparency if "
            u"you want to show an image."
        ),
        default="rgba(0,0,0,0)",
        vocabulary="collective.frontpage.SectionColors",
        required=True,
    )

    primary_color = schema.Choice(
        title=_(u"Primary Color"),
        default="#0083BE",
        description=_(u"Color for Icons and Buttons"),
        vocabulary="collective.frontpage.SectionColors",
        required=True,
    )

    background_image = NamedBlobImage(
        title=_(u"Background Image"),
        description=_(
            u"This will be a fullscreen-background for the section. "
            u"Make sure to set a semi-transparent or fully transparent "
            u"background-color to see the image."
        ),
        required=False,
    )

    link_url = schema.URI(
        title=_(u"Link"),
        description=_(u"The url to open when you click the main button"),
        required=False,
    )

    link_title = schema.TextLine(
        title=_(u"Linktitle"),
        description=_(u"The title for the main button"),
        required=False,
    )


class Section(Container):

    pass
