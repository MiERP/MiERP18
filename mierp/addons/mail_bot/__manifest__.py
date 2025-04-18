# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

{
    'name': 'mierpBot',
    'version': '1.2',
    'category': 'Productivity/Discuss',
    'summary': 'Add mierpBot in discussions',
    'website': '127.0.0.1:8730/app/discuss',
    'depends': ['mail'],
    'auto_install': True,
    'installable': True,
    'data': [
        'views/res_users_views.xml',
        'data/mailbot_data.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'mail_bot/static/src/scss/mierpbot_style.scss',
        ],
    },
    'license': 'LGPL-3',
}
