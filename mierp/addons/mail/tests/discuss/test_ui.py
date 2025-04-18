# Part of mierp. See LICENSE file for full copyright and licensing details.

import mierp.tests
from mierp import Command
from mierp.addons.base.tests.common import HttpCaseWithUserDemo


@mierp.tests.tagged('post_install', '-at_install')
class TestUi(HttpCaseWithUserDemo):

    def test_01_mail_tour(self):
        self.start_tour("/mierp", 'discuss_channel_tour', login="admin")

    def test_02_mail_create_channel_no_mail_tour(self):
        self.env['res.users'].create({
            'email': '', # User should be able to create a channel even if no email is defined
            'groups_id': [Command.set([self.ref('base.group_user')])],
            'name': 'Test User',
            'login': 'testuser',
            'password': 'testuser',
        })
        self.start_tour("/mierp", 'discuss_channel_tour', login='testuser')

    # basic rendering test of the configuration menu in Discuss
    def test_03_mail_discuss_configuration_tour(self):
        self.start_tour("/mierp", "discuss_configuration_tour", login="admin")
