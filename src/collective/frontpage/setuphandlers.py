# -*- coding: utf-8 -*-
from io import BytesIO
from PIL import Image
from PIL import ImageColor
from PIL import ImageDraw
from plone import api
from plone.namedfile.file import NamedBlobImage
from Products.CMFPlone.interfaces import INonInstallable
from random import choice
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
    _create_news_section(frontpage)
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
        background_color=u"#0083BE",
        primary_color=u"#F5F5F5",
        link_url="https://github.com/collective/collective.frontpage",
        link_title="GitHub Homepage",
    )
    api.content.transition(obj=section, transition="publish")


def _create_news_section(frontpage):
    section = api.content.create(
        type="News",
        container=frontpage,
        id="section-news-default",
        title=u"Example News Section",
        description="This is an example of a event frontpage section.",
        background_color=u"#F5F5F5",
        primary_color=u"#0083BE",
    )
    api.content.transition(obj=section, transition="publish")
    for i in ('Blue', 'Yellow', 'Green'):
        ni = api.content.create(
            type="News Item",
            container=section,
            id="news-item-{0}".format(i).lower(),
            title=u"News Item {0}".format(i),
            description="This is an example News Item to show how the News Section looks.",  # noqa
            image=_create_lead_image(color=i.lower())
        )
        api.content.transition(obj=ni, transition="publish")


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


def _create_lead_image(size=(800, 450), color="blue"):
    """
    Borrowed from
    https://github.com/plone/ploneorg.core/blob/master/ploneorg/core/setuphandlers.py
    Creates an memory object containing an image.
    Expects a size tuple and PIL color.
    :param size: tuple of ints (width, height) default (800, 450)
    :param color: String or PIL color (r,g,b) tuple.
    :return: NamedBlobImage
    """
    # Create an image.
    im = Image.new("RGB", size, color=color)

    # Draw some lines
    draw = ImageDraw.Draw(im)
    color = ImageColor.getrgb(color)
    for i in range(9):
        factor = choice(range(8, 18, 1)) / 10.0
        stroke_color = (
            int(min(color[0] * factor, 255)),
            int(min(color[1] * factor, 255)),
            int(min(color[2] * factor, 255)),
        )
        draw.line(
            [
                (choice(range(0, size[0])), choice(range(0, size[1]))),
                (choice(range(0, size[0])), choice(range(0, size[1])))
            ],
            fill=stroke_color,
            width=int(size[1] / 5)
        )

    # 'Save' the file.
    sio = BytesIO()
    im.save(sio, format="PNG")
    sio.seek(0)

    # Create named blob image
    nbi = NamedBlobImage()
    nbi.data = sio.read()
    nbi.filename = u"example.png"

    return nbi


def _create_dummy_user():
    """Creates a dummy user for testing"""
    api.user.create(
        email="max.mustermann@testing.com",
        username="mmustermann",
        password="testing@collective.frontpage",
        properties={"fullname": u"Max Mustermann"},
    )
