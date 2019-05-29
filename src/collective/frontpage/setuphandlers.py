# -*- coding: utf-8 -*-
from collective.frontpage import config
from plone import api
from Products.CMFPlone.interfaces import INonInstallable
from random import choice
from zope.component import getUtility
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory


@implementer(INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return ["collective.frontpage:uninstall"]


def _create_dummy_user():
    """Creates a dummy user for testing"""
    api.user.create(
        email="max.mustermann@testing.com",
        username="mmustermann",
        password="testing@collective.frontpage",
        properties={"fullname": u"Max Mustermann"},
    )


def _remove_default_pages(portal):
    """Remove default pages"""
    try:
        default_pages = [
            portal.get("news"),
            portal.get("events"),
            portal.get("Members"),
            portal.get("front-page"),
        ]
        api.content.delete(objects=default_pages)
    except Exception:
        pass


def _create_frontpage(portal):
    frontpage = api.content.create(
        type="Frontpage", container=portal, id="frontpage", title=u"Frontpage"
    )
    api.content.transition(obj=frontpage, transition="publish")
    portal.setDefaultPage("frontpage")


def _create_sections(portal):
    frontpage = portal.get("frontpage", None)
    section_colors = getUtility(
        IVocabularyFactory, "collective.frontpage.SectionColors"
    )
    voc_colors = section_colors(portal)
    section_types = getUtility(IVocabularyFactory, "collective.frontpage.SectionTypes")
    voc_types = section_types(portal)
    if frontpage:
        for i in range(1, 5):
            num = "{0:0=2d}".format(i)
            section = api.content.create(
                type="Section",
                container=frontpage,
                id="section-{0}".format(num),
                title=u"Section {0}".format(num),
                description=choice(config.DUMMY_DESCRIPTIONS),
                section_type=choice(voc_types._terms).token,
                background_color=choice(voc_colors._terms).token,
                primary_color=choice(voc_colors._terms).token,
            )
            api.content.transition(obj=section, transition="publish")


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.
    portal = api.portal.get()
    _create_frontpage(portal)


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.


def clean(context):
    """Clean handler for the collective.frontpage:testing profile"""
    # Do something at the end of the clean installation of this package.


def demo(context):
    """Demo handler for the collective.frontpage:testing profile"""
    # Do something at the end of the demo installation of this package.
    portal = api.portal.get()
    _remove_default_pages(portal)
    _create_sections(portal)
    _create_dummy_user()


def testing(context):
    """Testing handler for the collective.frontpage:testing profile"""
    # Do something at the end of the testing installation of this package.
