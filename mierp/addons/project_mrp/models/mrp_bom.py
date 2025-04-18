# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    project_id = fields.Many2one('project.project')
