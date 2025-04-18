# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import api, models

class ResCompany(models.Model):
    _inherit = "res.company"

    @api.model
    def _get_employee_start_date_field(self):
        self.ensure_one()
        return 'first_contract_date'
