# -*- coding: utf-8 -*-
from mierp import api, fields, models, _


class View(models.Model):
    _inherit = 'ir.ui.view'
    type = fields.Selection(
        selection_add=[
            ('mianalysis', 'mi Analysis'),
            ('midashboard', 'mi Dashboard'),
        ]
    )

    def _get_view_info(self):
        return {
            'mianalysis': {'icon': 'fa fa-tachometer'},
            'midashboard': {'icon': 'fa fa-tachometer'}
        } | super()._get_view_info()

# class ActWindowView(models.Model):
#     _inherit = 'ir.actions.act_window.view'
#     view_mode = fields.Selection(
#         selection_add=[
#             ('mianalysis', 'mi Analysis'),
#             ('midashboard', 'mi Dashboard'),
#         ],
#         ondelete={
#             'mianalysis': 'cascade',
#             'midashboard': 'cascade',
#         }
#     )
