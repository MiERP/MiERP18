# Part of mierp. See LICENSE file for full copyright and licensing details.
from mierp import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    l10n_cl_is_factoring = fields.Boolean('Factoring Company')
