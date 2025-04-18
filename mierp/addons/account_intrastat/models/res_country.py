# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class ResCountry(models.Model):
    _inherit = 'res.country'

    intrastat = fields.Boolean(string='Intrastat member')
