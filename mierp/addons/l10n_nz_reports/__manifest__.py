{
    'name': 'NZ - Accounting Reports',
    'version': '1.0',
    'category': 'Accounting/Localizations/Reporting',
    'description': """
Accounting reports for NZ
    """,
    'website': '127.0.0.1:8730/app/accounting',
    'depends': [
        'l10n_nz', 'account_reports'
    ],
    'installable': True,
    'auto_install': ['l10n_nz', 'account_reports'],
    'license': 'LGPL-3',
}
