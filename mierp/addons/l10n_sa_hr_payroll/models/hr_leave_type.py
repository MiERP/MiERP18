# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class HrLeaveType(models.Model):
    _inherit = "hr.leave.type"

    l10n_sa_is_compensable = fields.Boolean(string="Is Eligible for KSA Paid Compensation?")
