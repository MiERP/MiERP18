# Part of mierp. See LICENSE file for full copyright and licensing details.
from mierp import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    taxable_supply_date = fields.Date()
