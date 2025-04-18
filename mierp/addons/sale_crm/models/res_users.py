# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    target_sales_invoiced = fields.Integer('Invoiced in Sales Orders Target')
