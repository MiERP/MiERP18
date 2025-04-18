# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    partner_company_name = fields.Char(string='Company Name', related='partner_id.company_name', store=True, readonly=False)
