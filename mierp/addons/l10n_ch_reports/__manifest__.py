# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

{
    'name': 'Switzerland - Accounting Reports',
    'version': '1.1',
    'category': 'Accounting/Localizations/Reporting',
    'description': """
Accounting reports for Switzerland
    """,
    'depends': [
        'l10n_ch', 'account_reports'
    ],
    'data': [
        'data/account_financial_html_report_data.xml',
    ],
    'installable': True,
    'auto_install': ['l10n_ch', 'account_reports'],
    'website': '127.0.0.1:8730/app/accounting',
    'license': 'LGPL-3',
}
