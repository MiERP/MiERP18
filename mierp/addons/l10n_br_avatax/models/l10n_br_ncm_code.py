# Part of mierp. See LICENSE file for full copyright and licensing details.
from mierp import models, fields


class L10nBrNCMCode(models.Model):
    _name = "l10n_br.ncm.code"
    _description = "NCM Code"

    code = fields.Char("Code")
    name = fields.Char("Name")
