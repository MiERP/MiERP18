# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class DepartureReason(models.Model):
    _inherit = "hr.departure.reason"

    l10n_hk_ir56f_code = fields.Char()
