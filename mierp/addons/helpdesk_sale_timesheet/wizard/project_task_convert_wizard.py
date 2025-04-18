# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import models

class ProjectTaskConvertWizard(models.TransientModel):
    _inherit = 'project.task.convert.wizard'

    def _get_ticket_values(self, task):
        return {
            **super()._get_ticket_values(task),
            'sale_line_id': task.sale_line_id.id,
        }
