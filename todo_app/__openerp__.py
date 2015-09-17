# -*- coding: utf-8 -*-
{
    'name': "To-Do Application",

    'summary': """""",

    'description': """
        Manage your personal Tasks with this module.
    """,

    'author': "Beijing SSWY",
    'website': "http://www.sswyuan.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'todo_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
    'application': True,
}
