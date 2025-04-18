# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    hr_presence_last_compute_date = fields.Datetime()
