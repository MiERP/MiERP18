# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.
from mierp import fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    ep_order_ref = fields.Char("Easypost Order Reference", copy=False)
