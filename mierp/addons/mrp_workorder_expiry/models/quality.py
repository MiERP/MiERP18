# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class QualityCheck(models.Model):
    _inherit = 'quality.check'

    is_expired = fields.Boolean(related='lot_id.product_expiry_alert')
