from mierp import models, fields, api, _
from mierp.exceptions import UserError

class ResCompany(models.Model):
    _inherit = 'res.company'

    mi_lab_api_key = fields.Char('mi Lab API Key')

class miLabAPIKeyWizard(models.TransientModel):
    _name = 'mi.lab.api.key.wizard'
    _description = 'mi Lab API Key Wizard'

    mi_lab_api_key = fields.Char('mi Lab API Key')

    # Default Get
    def default_get(self, fields):
        res = super(miLabAPIKeyWizard, self).default_get(fields)
        company = self.env.user.company_id
        res['mi_lab_api_key'] = company.mi_lab_api_key
        return res

    def action_update_mi_lab_api_key(self):
        company = self.env.user.company_id
        company.mi_lab_api_key = self.mi_lab_api_key
        return True
    
    def action_access_mi_lab(self):
        mi_lab_url = self.env['ir.config_parameter'].sudo().get_param('mi_lab_url')
        return {
            'type': 'ir.actions.act_url',
            'url': mi_lab_url + '/web/login',
            'target': 'new',
        }

    