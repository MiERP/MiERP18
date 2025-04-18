# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    batch_payroll_move_lines = fields.Boolean(string="Batch Payroll Move Lines")
