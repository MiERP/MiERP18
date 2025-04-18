# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class Website(models.Model):
    _inherit = 'website'

    wa_sale_template_id = fields.Many2one('whatsapp.template', domain=[('model', '=', 'sale.order'), ('status', '=', 'approved')])
