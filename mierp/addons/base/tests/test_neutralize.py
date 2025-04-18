# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp.modules import neutralize

from mierp.tests import tagged
from mierp.tests.common import TransactionCase


@tagged('post_install', '-at_install', 'neutralize')
class TestNeutralize(TransactionCase):
    def test_10_neutralize(self):
        """ Simply testing that none of the SQL neutralize crashes """
        installed_modules = neutralize.get_installed_modules(self.cr)
        queries = neutralize.get_neutralization_queries(installed_modules)
        for query in queries:
            self.cr.execute(query)
