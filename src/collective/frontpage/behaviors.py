# -*- coding: utf-8 -*-

from collective.frontpage import _
from plone.autoform.interfaces import IFormFieldProvider
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from zope import schema
from zope.interface import alsoProvides
from zope.interface import Interface


class IImageFields(model.Schema):

    background_image = NamedBlobImage(
        title=_(u"Background Image"),
        description=_(
            u"This sets a background image to an item. "
            u"Make sure to use a semi-transparent or fully transparent "
            u"background-color to see the image."
        ),
        required=False,
    )


alsoProvides(IImageFields, IFormFieldProvider)


class IImageFieldsMarker(Interface):
    """
    Marker interface that will be provided by instances using the
    IImageFields behavior.
    """


class IColorFields(model.Schema):

    background_color = schema.Choice(
        title=_(u"Background Color"),
        description=_(
            u"The background-color will always be on top of the "
            u"background-image. Make sure to use transparency if "
            u"you want to the image."
        ),
        default=u"rgba(0,0,0,0)",
        vocabulary="collective.frontpage.SectionColors",
        required=True,
    )

    primary_color = schema.Choice(
        title=_(u"Primary Color"),
        default=u"#0083BE",
        description=_(u"The primary color used for text, icons and buttons."),
        vocabulary="collective.frontpage.SectionColors",
        required=True,
    )


alsoProvides(IColorFields, IFormFieldProvider)


class IColorFieldsMarker(Interface):
    """
    Marker interface that will be provided by instances using the
    IColorFields behavior.
    """


class ILinkFields(model.Schema):

    link_url = schema.URI(
        title=_(u"Link URL"),
        required=False,
    )

    link_title = schema.TextLine(
        title=_(u"Link Title"),
        required=False,
    )


alsoProvides(ILinkFields, IFormFieldProvider)


class ILinkFieldsMarker(Interface):
    """
    Marker interface that will be provided by instances using the
    ILinkFields behavior.
    """
