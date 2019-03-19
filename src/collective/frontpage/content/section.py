# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from collective.frontpage import _
from plone.namedfile.field import NamedBlobImage


class ISection(model.Schema):
    """
    Marker interface and Dexterity Python Schema for Section
    """

    section_type = schema.Choice(
        title=_(u'Type'),
        default='static',
        vocabulary='collective.frontpage.SectionTypes',
        required=True,
    )

    background_color = schema.Choice(
        title=_(u'Background Color'),
        default='#0083BE',
        vocabulary='collective.frontpage.SectionBackgroundColors',
        required=True,
    )

    background_image = NamedBlobImage(
        title=_(u'Background Image'),
        required=False,
    )

    link_url = schema.URI(
        title=_(u'Link'),
        required=False,
    )

    link_title = schema.TextLine(
        title=_(u'Linktitle'),
        required=False,
    )


class Section(Container):

    pass
