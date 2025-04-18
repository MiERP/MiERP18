# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import api, models
from mierp.osv import expression


class SaleOrderTemplateOption(models.Model):
    _inherit = 'sale.order.template.option'

    @api.model
    def _product_id_domain(self):
        """ Override to allow users to add a rental product as a quotation template option """
        return expression.OR([super()._product_id_domain(), [('rent_ok', '=', True)]])
