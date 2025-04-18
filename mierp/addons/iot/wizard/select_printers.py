# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models

class SelectPrinter(models.TransientModel):
    _name = "select.printers.wizard"
    _description = "Selection of printers"

    device_ids = fields.Many2many('iot.device', domain=[('type', '=', 'printer')])
    display_device_ids = fields.Many2many('iot.device', relation='display_device_id_select_printer', domain=[('type', '=', 'printer')])
