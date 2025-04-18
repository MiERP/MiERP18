# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class Website(models.Model):
    _inherit = 'website'

    newsletter_id = fields.Many2one(string="Newsletter List", comodel_name='mailing.list')
