# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class FleetVehicleOdometer(models.Model):
    _inherit = 'fleet.vehicle.odometer'

    driver_employee_id = fields.Many2one(
        related='vehicle_id.driver_employee_id', string='Driver (Employee)',
        readonly=True,
    )
