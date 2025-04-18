# -*- coding: utf-8 -*-
# Copyright 2022 MiERP
from mierp import models, fields


class miAnalysisVisualConfig(models.Model):
    _name = 'mi.analysis.visual.config'
    _description = 'mi Analysis Visual Config'

    analysis_id = fields.Many2one(comodel_name='mi.analysis', string='Analysis', ondelete='cascade')
    visual_config_id = fields.Many2one(comodel_name='mi.visual.config', string='Visual Config')
    visual_config_value_id = fields.Many2one(comodel_name='mi.visual.config.value', string='Visual Config Value')
    string_value = fields.Text(string='String Value')
