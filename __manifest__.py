# -*- coding: utf-8 -*-
{
    'name': "Wolftrak Project",

    'summary': """
        Personalización a el modulo de projectos para WolftrakGlobal
        """,

    'description': """
        Personalización a el modulo de projectos para WolftrakGlobal
    """,

    'author': "Artech SAC",
    'website': "http://www.artech.pe",

    'category': 'project',
    'version': '0.1',

    'depends': ['base', 'project'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/project_views.xml',
        'views/res_views.xml',
    ],
}