# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import models


class MailTemplate(models.Model):
    _name = 'mail.template'
    _description = 'Email Templates'
    _inherit = ['studio.mixin', 'mail.template']
