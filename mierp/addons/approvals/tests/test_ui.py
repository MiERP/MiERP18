# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp.tests import tagged
from mierp.addons.base.tests.common import HttpCaseWithUserDemo


@tagged('-at_install', 'post_install')
class TestUi(HttpCaseWithUserDemo):

    def test_ui(self):
        self.env.ref('approvals.approval_category_data_business_trip').write({
            'approver_ids': [(5, 0, 0), (0, 0, {'user_id': self.env.ref('base.user_admin').id})],
        })
        self.start_tour("/mierp", 'approvals_tour', login='admin')
