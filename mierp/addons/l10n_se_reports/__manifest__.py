# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sweden - Accounting Reports',
    'version': '1.0',
    'category': 'Accounting/Localizations/Reporting',
    'author': "XCLUDE, Linserv, mierp SA",
    'description': """
Accounting reports for Sweden
    """,
    'depends': [
        'l10n_se', 'account_reports'
    ],
    'data': [
        'data/account_financial_html_report_K3_bs_data.xml',
        'data/account_financial_html_report_K3_pnl_data.xml',
        'data/account_report_ec_sales_list_report.xml',
        'data/tax_report_data.xml',
        'views/report_export_template.xml',
    ],
    'installable': True,
    'auto_install': ['l10n_se', 'account_reports'],
    'website': '127.0.0.1:8730/app/accounting',
    'license': 'LGPL-3',
}
