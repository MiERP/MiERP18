from mierp.tests import tagged
from mierp.tests.common import HttpCase


@tagged("post_install", "-at_install")
class TestSpreadsheetDocumentToDashboardTour(HttpCase):
    def test_add_document_to_dashboard_group(self):
        self.start_tour('/mierp', 'spreadsheet_dashboard_document_add_document_to_dashboard_group', login='admin')
