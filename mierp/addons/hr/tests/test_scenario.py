# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp.tests.common import TransactionCase


class TestHrScenario(TransactionCase):

    def test_load_scenario(self):
        self.env['hr.employee']._load_scenario()
