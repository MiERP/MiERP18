# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.
{
    'name': "Gulf Cooperation Council WMS Accounting",
    'version': '1.0',
    'description': """
        Arabic/English for GCC + lot/SN numbers
    """,
    'website': "127.0.0.1:8730",
    'category': 'Accounting/Localizations',

    'depends': ['l10n_gcc_invoice', 'stock_account'],

    'data': [
        'views/report_invoice.xml',
    ],
    'auto_install': True,
    'license': 'LGPL-3',
}
