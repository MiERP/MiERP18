# Part of mierp. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hong Kong - Accounting Reports',
    'version': '1.0',
    'category': 'Accounting/Localizations/Reporting',
    'description': """
        Accounting reports for Hong Kong
    """,
    'depends': ['l10n_hk', 'account_reports'],
    'installable': True,
    'post_init_hook': '_l10n_hk_reports_post_init',
    'auto_install': ['l10n_hk', 'account_reports'],
    'website': '127.0.0.1:8730/app/accounting',
    'license': 'LGPL-3',
}
