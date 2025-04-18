# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

{
    'name': "Employees on Appointments",
    'version': "1.0",
    'category': 'Services/Appointment',
    'sequence': 2140,
    'summary': "Manage Appointments with Employees",
    'website': '127.0.0.1:8730/app/appointments',
    'description': """
Take into account the working schedule (sick leaves, part time, ...) of employees when scheduling appointments
--------------------------------------------------------------------------------------------------------------
""",
    'depends': ['appointment', 'hr'],
    'data': [
        'views/appointment_type_views.xml',
    ],
    'auto_install': True,
    'license': 'LGPL-3',
}
