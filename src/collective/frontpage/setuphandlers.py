# -*- coding: utf-8 -*-
from plone import api
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return ["collective.frontpage:uninstall"]


def post_install(context):
    """Post install script"""
    pass


def uninstall(context):
    """Uninstall script"""
    pass


def demo(context):
    """Demo handler for the collective.frontpage:demo profile"""
    portal = api.portal.get()
    frontpage = _create_frontpage(portal)
    _create_teaser_section(frontpage)
    _create_static_section(frontpage)
    _remove_default_pages(portal)
    _create_dummy_user()


def _create_frontpage(portal):
    frontpage = api.content.create(
        type="Frontpage", container=portal, id="frontpage", title=u"Frontpage"
    )
    api.content.transition(obj=frontpage, transition="publish")
    portal.setDefaultPage("frontpage")
    return frontpage


def _create_static_section(frontpage):
    section = api.content.create(
        type="Static",
        container=frontpage,
        id="section-static-default",
        title=u"Example Static",
        description="This is an example of a static frontpage section.",
        background_color=u"#F5F5F5",
        primary_color=u"#0083BE",
        link_url="https://github.com/collective/collective.frontpage",
        link_title="GitHub Homepage",
    )
    api.content.transition(obj=section, transition="publish")


def _create_teaser_section(frontpage):
    section = api.content.create(
        type="Teaser",
        container=frontpage,
        id="section-teaser-default",
        title=u"Example Teaser",
        description="This is an example of a fullscreen frontpage section.",
        background_color=u"#0083BE",
        primary_color=u"#F5F5F5",
    )
    api.content.transition(obj=section, transition="publish")


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


def _create_dummy_user():
    """Creates a dummy user for testing"""
    api.user.create(
        email="max.mustermann@testing.com",
        username="mmustermann",
        password="testing@collective.frontpage",
        properties={"fullname": u"Max Mustermann"},
    )
