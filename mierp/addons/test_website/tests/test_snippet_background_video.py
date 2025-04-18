# Part of mierp. See LICENSE file for full copyright and licensing details.

import mierp.tests


@mierp.tests.common.tagged('post_install', '-at_install')
class TestSnippetBackgroundVideo(mierp.tests.HttpCase):

    def test_snippet_background_video(self):
        self.start_tour("/", "snippet_background_video", login="admin")
