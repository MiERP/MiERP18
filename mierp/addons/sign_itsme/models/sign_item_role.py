# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models

class SignItemParty(models.Model):
    _inherit = "sign.item.role"

    auth_method = fields.Selection(selection_add=[
        ('itsme', 'Via itsme®')
    ], ondelete={'itsme': 'cascade'})
