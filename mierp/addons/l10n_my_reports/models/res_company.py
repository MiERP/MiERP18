# Part of mierp. See LICENSE file for full copyright and licensing details.

from mierp import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    l10n_my_description = fields.Html(string='Statement of Account report description', translate=True)
