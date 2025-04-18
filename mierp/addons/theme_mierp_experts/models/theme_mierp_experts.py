from mierp import models


class ThememierpExperts(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_mierp_experts_post_copy(self, mod):
        self.enable_view('website.template_footer_contact')
