# Part of mierp. See LICENSE file for full copyright and licensing details.
from mierp.tests import tagged, HttpCase


@tagged('post_install', '-at_install')
class TestExpensesTour(HttpCase):
    def test_tour_expenses(self):
        self.start_tour("/mierp", "hr_expense_test_tour", login="admin")
