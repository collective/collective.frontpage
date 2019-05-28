# -*- coding: utf-8 -*-
from collective.frontpage import _
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from zope import schema
from zope.interface import Interface


class ISettings(Interface):

    section_colors = schema.List(
        title=_(u"frontpage_settings_section_colors_title", default="Section Colors"),
        value_type=schema.TextLine(),
        required=True,
        default=[
            u"Default | rgba(0,0,0,1)",
            u"Plone Blue | #0083BE",
            u"Dirty White | #F5F5F5",
            u"Red | rgb(255,0,0)",
            u"Semi Transparent | rgba(0,0,0,0.5)",
            u"Red Transparent | rgba(255,0,0,0.5)",
            u"Dark Blue RGB | rgb(25,25,112)",
            u"Light Green RGB | rgb(173,255,47)",
        ],
    )


class SettingsEditForm(RegistryEditForm):
    schema = ISettings
    schema_prefix = "collective.frontpage"
    label = _(u"frontpage_settings_title", default=u"Frontpage Settings")


SettingsView = layout.wrap_form(SettingsEditForm, ControlPanelFormWrapper)
