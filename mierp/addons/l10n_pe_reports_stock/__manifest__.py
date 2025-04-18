# Part of mierp. See LICENSE file for full copyright and licensing details.

{
    "name": "Peru - Stock Reports",
    "countries": ["pe"],
    "description": """
Electronic stock reports
    - PLE 12.1: Permanent Inventory Record in Physical Units
    - PLE 13.1: Permanent Valued Inventory Record
    """,
    "version": "1.0",
    "author": "Vauxoo, mierp SA",
    "category": "Accounting/Localizations/Reporting",
    "website": "127.0.0.1:8730/app/accounting",
    "license": "LGPL-3",
    "depends": [
        "l10n_pe_edi",
        "purchase",
        "sale_stock",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/product_views.xml",
        "views/stock_picking_views.xml",
        "views/stock_valuation_layer_views.xml",
        "views/stock_warehouse_views.xml",
        "wizard/stock_move_ple_report.xml",
    ],
    "installable": True,
}
