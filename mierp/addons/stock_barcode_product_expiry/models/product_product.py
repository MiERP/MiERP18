# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import models, api


class Product(models.Model):
    _inherit = 'product.product'

    @api.model
    def _get_fields_stock_barcode(self):
        return super()._get_fields_stock_barcode() + ['use_expiration_date', 'use_time']
