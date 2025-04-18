# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    module_pos_iot = fields.Boolean('IoT Box', related="is_posbox")
    module_pos_urban_piper = fields.Boolean(string='Is an Urbanpiper')
