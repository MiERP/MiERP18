import mierp.tests
from mierp.tools import mute_logger


@mierp.tests.common.tagged('post_install', '-at_install')
class TestWebsiteError(mierp.tests.HttpCase):

    @mute_logger('mierp.addons.http_routing.models.ir_http', 'mierp.http')
    def test_01_run_test(self):
        self.start_tour("/test_error_view", 'test_error_website')
