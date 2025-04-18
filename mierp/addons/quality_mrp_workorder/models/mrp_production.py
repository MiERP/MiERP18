# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    check_ids = fields.One2many('quality.check', domain=[('workorder_id', '=', False)])
