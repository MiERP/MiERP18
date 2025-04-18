# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models, tools


class MailingTraceReport(models.Model):
    _inherit = 'mailing.trace.report'

    def _report_get_request_where_items(self):
        res = super(MailingTraceReport, self)._report_get_request_where_items()
        res.append("mailing.use_in_marketing_automation IS NOT TRUE")
        return res
