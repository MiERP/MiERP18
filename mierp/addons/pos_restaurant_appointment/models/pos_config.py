  # -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    appointment_type_id = fields.Many2one('appointment.type', string='Appointment Type')
