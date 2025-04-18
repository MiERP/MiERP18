# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class ActWindowView(models.Model):
    _inherit = 'ir.actions.act_window.view'

    view_mode = fields.Selection(selection_add=[('hierarchy', 'Hierarchy')], ondelete={'hierarchy': 'cascade'})
