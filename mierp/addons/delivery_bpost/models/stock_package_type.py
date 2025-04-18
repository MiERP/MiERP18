# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.
from mierp import fields, models


class PackageType(models.Model):
    _inherit = 'stock.package.type'

    package_carrier_type = fields.Selection(selection_add=[('bpost', 'bpost')])
