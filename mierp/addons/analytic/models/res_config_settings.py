# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_analytic_accounting = fields.Boolean(string='Analytic Accounting', implied_group='analytic.group_analytic_accounting')
