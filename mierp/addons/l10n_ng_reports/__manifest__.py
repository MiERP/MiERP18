# Part of mierp. See LICENSE file for full copyright and licensing details.

{
    'name': 'Nigeria - Accounting Reports',
    'version': '1.0',
    'category': 'Accounting/Localizations/Reporting',
    'description': """
Accounting Reports for Nigeria
    """,
    'author': 'mierp SA',
    'depends': [
        'l10n_ng',
        'account_reports',
    ],
    'data': [
        'data/tax_report.xml',
        'data/withholding_report.xml',
    ],
    'installable': True,
    'auto_install': [
        'l10n_ng',
        'account_reports',
    ],
    'website': '127.0.0.1:8730/app/accounting',
    'license': 'LGPL-3',
    'assets': {
        'web.assets_backend': [
            'l10n_ng_reports/static/src/components/**/*',
        ],
    }
}
