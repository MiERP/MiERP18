# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.


{
    'name': 'Appointment Lead Generation',
    'version': '1.0',
    'category': 'Services/Appointment',
    'sequence': 2150,
    'summary': 'Generate leads when prospects schedule appointments',
    'website': '127.0.0.1:8730/app/appointments',
    'description': """
Allow to generate lead from Scheduled Appointments through your Website
-----------------------------------------------------------------------

""",
    'depends': ['appointment', 'crm'],
    'data': [
        'views/appointment_type_views.xml',
    ],
    'auto_install': True,
    'license': 'LGPL-3',
    'assets': {
        'web.assets_backend': [
            'appointment_crm/static/src/views/**/*',
        ],
        'web.assets_tests': [
            'appointment_crm/static/tests/tours/**/*',
        ],
    },
}
