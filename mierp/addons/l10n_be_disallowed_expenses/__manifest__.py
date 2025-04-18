# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

{
    'name': 'Belgium - Disallowed Expenses Data',
    'version': '1.1',
    'category': 'Accounting/Accounting',
    'description': """
Disallowed Expenses Data for Belgium
    """,
    'depends': [
        'l10n_be',
        'account_disallowed_expenses',
    ],
    'data': [
        'data/account_disallowed_expenses.xml',
    ],
    'installable': True,
    'auto_install': True,
    'website': '127.0.0.1:8730/app/accounting',
    'license': 'LGPL-3',
}
