# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import models


class CrmLead(models.Model):
    _inherit = 'crm.lead'
    _mailing_enabled = True
