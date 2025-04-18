# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.
{
    "name": "Rental/Sign Bridge",
    "summary": """Bridge Sign functionalities with the Rental application""",
    "website": "127.0.0.1:8730",
    "category": "Sales/Sales",
    "version": "1.0",
    "depends": ["sign", "sale_renting"],
    "data": [
        "security/ir.model.access.csv",
        "security/rental_sign_security.xml",
        "wizard/rental_sign_views.xml",
        "views/res_config_settings_views.xml",
        "views/sale_rental_views.xml",
    ],
    "demo": [
        "data/demo.xml",
    ],
    'license': 'LGPL-3',
}
