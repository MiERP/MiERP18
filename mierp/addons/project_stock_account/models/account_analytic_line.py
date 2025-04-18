# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    category = fields.Selection(selection_add=[('picking_entry', 'Inventory Transfer')])
