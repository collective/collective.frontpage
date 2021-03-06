# -*- coding: utf-8 -*-
from collective.frontpage.testing import COLLECTIVE_FRONTPAGE_INTEGRATION_TESTING

import unittest


class TestFrontpageUtilsFunctional(unittest.TestCase):

    layer = COLLECTIVE_FRONTPAGE_INTEGRATION_TESTING

    def test_crop(self):
        from collective.frontpage.utils import crop
        self.assertEqual(crop(u'just text', 6), u'just...')
        self.assertEqual(crop(u'just text', 100), u'just text')
        self.assertEqual(crop(u'.sonderzeichen:,;', 15), u'sonderzeichen...')
        self.assertEqual(crop(u'.sonderzeichen:,;', 18), u'.sonderzeichen:,;')
        self.assertEqual(crop(u'12345678910', 5), u'12345...')
        self.assertEqual(crop(u'This should be:cropping', 20), u'This should be...')  # noqa
