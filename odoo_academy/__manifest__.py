{
    'name': "Odoo Academy",
    'summary': """Academy App to manage training""",
    'description': """
        Adademy Module to manage training:
            - Sessions
            - Courses
            - Attendees
    """,
    'author': 'Odoo',
    'website': 'https://www.odoo.com',
    'category': 'Training',
    'version': '0.1',
    'depends': ['sale'],
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitem.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sale_views_inherit.xml',

    ],

    'demo': ['demo/academy_demo.xml'

    ]

}
