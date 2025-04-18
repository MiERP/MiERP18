# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

{
    'name': 'Belgium - Accounting Reports (post wizard)',
    'version': '1.0',
    'category': 'Accounting/Localizations/Reporting',
    'description': """
Enable the VAT wizard when posting a tax return journal entry
    """,
    'depends': [
        'l10n_be_reports'
    ],
    'data': [
        'data/res_partner.xml',
        'security/ir.model.access.csv',
        'views/l10n_be_wizard_xml_export_options_views.xml',
        'wizard/vat_pay_wizard.xml',
    ],
    'installable': True,
    'auto_install': True,
    'website': '127.0.0.1:8730/app/accounting',
    'license': 'LGPL-3',
}
