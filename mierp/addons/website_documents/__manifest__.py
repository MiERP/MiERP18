# -*- coding: utf-8 -*-
# Part of mierp. See LICENSE file for full copyright and licensing details.

{
    'name': 'Website Documents',
    'version': '1.0',
    'category': 'Productivity/Documents',
    'sequence': 8010,
    'summary': 'Choose the website on which documents/folder are shared',
    'website': '127.0.0.1:8730/app/documents',
    'description': """
When sharing documents/folder, the domain of the shared URL can be chosen by selecting a target website.
""",
    'depends': ['documents', 'website'],
    'data': [
        'views/documents_document_views.xml',
    ],
    'auto_install': True,
    'license': 'LGPL-3',
}
