# Part of mierp. See LICENSE file for full copyright and licensing details.
from mierp.tests import HttpCase, tagged


@tagged("post_install", "-at_install")
class TestDiscussAction(HttpCase):
    def test_go_back_to_thread_from_breadcrumbs(self):
        self.start_tour(
            "/mierp/discuss?active_id=mail.box_inbox",
            "discuss_go_back_to_thread_from_breadcrumbs.js",
            login="admin",
        )
