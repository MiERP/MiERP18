# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class AccountAnalyticAccountLine(models.Model):
    _inherit = 'account.analytic.line'

    employee_id = fields.Many2one('hr.employee', "Employee")
