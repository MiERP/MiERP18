# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.
from mierp import fields, models


class AccountTaxGroup(models.Model):
    _inherit = 'account.tax.group'

    l10n_pe_edi_code = fields.Char('EDI Code', help="Peruvian EDI code to complement catalog 05")
