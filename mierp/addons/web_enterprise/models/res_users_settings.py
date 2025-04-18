# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class ResUsersSettings(models.Model):
    _inherit = 'res.users.settings'

    homemenu_config = fields.Json(string="Home Menu Configuration", readonly=True)
