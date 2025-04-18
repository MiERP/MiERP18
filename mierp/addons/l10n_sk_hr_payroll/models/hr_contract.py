# -*- coding:utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class HrContract(models.Model):
    _inherit = 'hr.contract'

    l10n_sk_meal_voucher_employee = fields.Monetary("Meal Vouchers Amount (Employee)")
    l10n_sk_meal_voucher_employer = fields.Monetary("Meal Vouchers Amount (Employer)")
