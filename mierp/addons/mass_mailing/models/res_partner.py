# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import models


class Partner(models.Model):
    _inherit = 'res.partner'
    _mailing_enabled = True
