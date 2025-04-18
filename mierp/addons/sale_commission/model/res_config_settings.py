# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # Todo MASTER: remove as forecast are displayed in report
    group_commission_forecast = fields.Boolean("Achievement Forecast", implied_group='sale_commission.group_commission_forecast')
