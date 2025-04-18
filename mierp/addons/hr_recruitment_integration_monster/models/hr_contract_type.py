# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import models, fields


class HrContractType(models.Model):
    _inherit = 'hr.contract.type'

    monster_id = fields.Integer(
        string='Monster ID', help='Monster ID of the contract type.')
