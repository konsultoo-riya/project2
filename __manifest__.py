
{
    'name': "Duplicate Customer",
    'summary': """Remove Duplicate Contacts""",
    'version': '14.0.0.1.0',
    'category': 'Contacts',

    'depends': ['base', 'contacts', 'calendar'],
    'data': [
        'data/data.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'images': ['static/description/poster_image.png'],
}
