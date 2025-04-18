# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_delivery_shiprocket = fields.Boolean("Shiprocket Connector")
