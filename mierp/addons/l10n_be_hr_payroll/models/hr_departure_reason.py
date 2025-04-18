# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class DepartureReason(models.Model):
    _inherit = "hr.departure.reason"

    def _get_default_departure_reasons(self):
        return {
            **super()._get_default_departure_reasons(),
            'freelance': 350,
        }
