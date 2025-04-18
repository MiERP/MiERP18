# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class FollowupLine(models.Model):
    _inherit = 'account_followup.followup.line'

    send_letter = fields.Boolean('Send a Letter', default=False)
