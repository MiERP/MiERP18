# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import models, fields


class CommissionPlanAchievement(models.Model):
    _inherit = 'sale.commission.plan.achievement'

    type = fields.Selection(selection_add=[('margin', "Margin")], ondelete={'margin': 'cascade'})
