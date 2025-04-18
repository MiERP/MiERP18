# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class AccountTaxReportActivityType(models.Model):
    _inherit = "mail.activity.type"

    category = fields.Selection(selection_add=[('tax_report', 'Tax report')])
