# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import models


class IrDefault(models.Model):
    _name = 'ir.default'
    _inherit = ['studio.mixin', 'ir.default']
