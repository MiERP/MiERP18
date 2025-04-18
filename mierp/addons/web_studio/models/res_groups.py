# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import models


class Groups(models.Model):
    _name = 'res.groups'
    _inherit = ['studio.mixin', 'res.groups']
