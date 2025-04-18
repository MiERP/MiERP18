# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

import mierp.tests

@mierp.tests.tagged("post_install", "-at_install")
class TestmierpEditor(mierp.tests.HttpCase):

    def test_mierp_editor_suite(self):
        self.browser_js('/web_editor/tests', "", "", login='admin', timeout=1800)
