# -*- coding: utf-8 -*-
# Copyright 2022 MiERP
from mierp import models, fields


class miVisualConfigValue(models.Model):
    _name = 'mi.visual.config.value'
    _description = 'mi Visual Config Value'

    name = fields.Char('Name', required=True)
    title = fields.Char('Title', required=True)
    value_type = fields.Selection([
        ('string', 'String'),
        ('number', 'Number'),
        ('boolean', 'Boolean'),
    ])
    visual_config_ids = fields.Many2many(comodel_name='mi.visual.config', string='Visual Config')
