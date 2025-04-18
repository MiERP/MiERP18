# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import models


class IrFilters(models.Model):
    _name = 'ir.filters'
    _inherit = ['studio.mixin', 'ir.filters']
