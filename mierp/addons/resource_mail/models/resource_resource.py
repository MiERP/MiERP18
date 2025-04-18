# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class ResourceResource(models.Model):
    _inherit = 'resource.resource'

    im_status = fields.Char(related='user_id.im_status')
