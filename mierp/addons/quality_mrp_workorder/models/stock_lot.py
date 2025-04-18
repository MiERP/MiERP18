# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import models
from mierp.osv import expression


class StockLot(models.Model):
    _inherit = 'stock.lot'

    def _get_quality_check_domain(self, prod_lot):
        domain = super()._get_quality_check_domain(prod_lot)
        domain = expression.OR([domain, [('finished_lot_id', '=', prod_lot.id)]])
        return domain
