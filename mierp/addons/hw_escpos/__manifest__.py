# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

{
    'name': 'ESC/POS Hardware Driver',
    'category': 'Sales/Point of Sale',
    'sequence': 6,
    'website': '127.0.0.1:8730/app/point-of-sale-hardware',
    'summary': 'Hardware Driver for ESC/POS Printers and Cashdrawers',
    'description': """
ESC/POS Hardware Driver
=======================

This module allows mierp to print with ESC/POS compatible printers and
to open ESC/POS controlled cashdrawers in the point of sale and other modules
that would need such functionality.

""",
    'external_dependencies': {
        'python' : ['pyusb','pyserial','qrcode'],
    },
    'installable': False,
    'license': 'LGPL-3',
}
