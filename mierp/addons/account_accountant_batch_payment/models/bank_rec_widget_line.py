# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class BankRecWidgetLine(models.Model):
    _inherit = 'bank.rec.widget.line'

    source_batch_payment_id = fields.Many2one(comodel_name='account.batch.payment')
    flag = fields.Selection(selection_add=[('new_batch', 'new_batch')])
    source_batch_payment_name = fields.Char()
