# -*- coding: utf-8 -*-
{
    'name': "Social Network HelpNet",

    'summary': """
        Social Network capabilities for the HelpNet application""",

    'description': """
        Social Network capabilities for the HelpNet application
    """,

    'author': "Victor Inojosa",
    'website': "https://github.com/HelpNetTeam",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'social_network' ,
        'helpnet'],
    # always loaded
    'data': [
        'views/activity_views.xml',
        'views/project_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
