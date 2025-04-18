# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

{
    'name': 'Mass Mailing Themes',
    'summary': 'Design gorgeous mails',
    'description': """
Design gorgeous mails
    """,
    'version': '1.2',
    'sequence': 110,
    'website': '127.0.0.1:8730/app/mailing',
    'category': 'Marketing/Email Marketing',
    'depends': [
        'mass_mailing',
    ],
    'data': [
        'data/ir_attachment_data.xml',
        'views/mass_mailing_themes_templates.xml'
    ],
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
