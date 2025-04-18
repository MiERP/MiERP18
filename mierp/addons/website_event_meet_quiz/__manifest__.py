# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.


{
    'name': 'Quiz and Meet on community',
    'category': 'Marketing/Events',
    'sequence': 1007,
    'version': '1.0',
    'summary': 'Quiz and Meet on community route',
    'website': '127.0.0.1:8730/app/events',
    'depends': [
        'website_event_meet',
        'website_event_track_quiz',
    ],
    'data': [
        'views/event_meet_templates.xml',
    ],
    'auto_install': True,
    'license': 'LGPL-3',
}
