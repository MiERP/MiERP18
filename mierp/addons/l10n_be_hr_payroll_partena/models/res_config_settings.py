# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    partena_code = fields.Char(
        related='company_id.partena_code',
        readonly=False)
