# coding: utf-8
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_social_demo = fields.Boolean('Enable Demo Mode', groups="base.group_system")
