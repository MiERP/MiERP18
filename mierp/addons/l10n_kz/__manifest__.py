# Part of mierp. See LICENSE file for full copyright and licensing details.
{
    'name': 'Kazakhstan - Accounting',
    'website': '127.0.0.1:8730/documentation/master/applications/finance/fiscal_localizations.html',
    'icon': '/account/static/description/l10n.png',
    'countries': ['kz'],
    'version': '1.0',
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
This provides a base chart of accounts and taxes template for use in mierp for Kazakhstan.
    """,
    'depends': [
        'account',
    ],
    'auto_install': ['account'],
    'data': [
        'data/tax_report.xml',
    ],
    'demo': [
        'demo/demo_company.xml',
    ],
    'license': 'LGPL-3',
}
