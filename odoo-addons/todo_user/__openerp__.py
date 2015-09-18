# -*- coding: utf-8 -*-
{
    'name': "Multiuser To-Do",

    'summary': """
        """,

    'description': """
        Extend the To-Do app to multiuser.
    """,

    'author': "BJWWSY",
    'website': "http://www.sswyuan.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['todo_app'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'todo_view.xml',
        'subtask_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}