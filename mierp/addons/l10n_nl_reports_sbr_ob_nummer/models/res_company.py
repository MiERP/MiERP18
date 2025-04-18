# Part of mierp. See LICENSE file for full copyright and licensing details.
from mierp import fields, models

class ResCompany(models.Model):

    _inherit = "res.company"

    l10n_nl_reports_sbr_ob_nummer = fields.Char('Omzetbelastingnummer', help="This number is used for contacts with the Tax Administration.")
