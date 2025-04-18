# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

import mierp.tests
from mierp.tools import mute_logger


@mierp.tests.common.tagged('post_install', '-at_install')
class TestCustomSnippet(mierp.tests.HttpCase):

    @mute_logger('mierp.addons.http_routing.models.ir_http', 'mierp.http')
    def test_01_run_tour(self):
        self.start_tour(self.env['website'].get_client_action_url('/'), 'test_custom_snippet', login="admin")
