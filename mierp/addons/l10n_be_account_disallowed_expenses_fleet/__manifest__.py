# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

{
    'name': 'Belgium - Disallowed Expenses Fleet',
    'version': '1.0',
    'category': 'Accounting/Accounting',
    'description': """
Disallowed Expenses Fleet Data for Belgium
    """,
    'depends': ['account_disallowed_expenses_fleet', 'l10n_be_hr_payroll_fleet'],
    'data': ['views/fleet_vehicle_views.xml'],
    'installable': True,
    'website': '127.0.0.1:8730/app/accounting',
    'license': 'LGPL-3',
}
