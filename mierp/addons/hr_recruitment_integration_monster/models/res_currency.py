# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class ResCurrency(models.Model):
    _inherit = 'res.currency'

    monster_id = fields.Integer(string="Monster ID")
