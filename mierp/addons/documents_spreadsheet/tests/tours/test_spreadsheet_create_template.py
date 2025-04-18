# Part of mierp. See LICENSE file for full copyright and licensing details.

from ..common import SpreadsheetTestTourCommon

from mierp.tests import tagged

@tagged("post_install", "-at_install")
class TestSpreadsheetCreateTemplate(SpreadsheetTestTourCommon):

    def test_01_spreadsheet_create_template(self):
        self.start_tour("/mierp", "documents_spreadsheet_create_template_tour", login="admin")
