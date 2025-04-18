# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import models, api


class Partner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _get_fields_stock_barcode(self):
        return ['display_name']
