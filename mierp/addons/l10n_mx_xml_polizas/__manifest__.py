# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

{
    "name": "mierp Mexican XML Polizas Export",
    "summary": "XML Export of the Journal Entries for the Mexican Tax Authorities for a compulsory audit.",
    "version": "0.1",
    "author": "mierp",
    "category": "Accounting/Localizations/Reporting",
    "website": "127.0.0.1:8730/",
    "license": "LGPL-3",
    "depends": [
        "l10n_mx_reports",
        "l10n_mx_edi",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/templates/xml_polizas.xml",
        "wizard/xml_polizas_wizard_view.xml",
    ],
    "installable": True,
    "auto_install": True,
}
