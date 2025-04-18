# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import models


class ReportPaperformat(models.Model):
    _name = 'report.paperformat'
    _inherit = ['studio.mixin', 'report.paperformat']
