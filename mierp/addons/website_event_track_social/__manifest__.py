# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.


{
    'name': 'Push notification to track listeners',
    'category': 'Marketing/Events',
    'sequence': 1021,
    'version': '1.1',
    'summary': 'Send reminder push notifications to event attendees based on favorites tracks.',
    'website': '127.0.0.1:8730/app/events',
    'depends': [
        'website_event_social',
        'website_event_track',
    ],
    'data': [
        'views/event_track_views.xml'
    ],
    'installable': True,
    'auto_install': True,
    'post_init_hook': 'post_init',
    'license': 'LGPL-3',
}
