# -*- coding: utf-8 -*-
{
    'name': "Test Matrix",

    'summary': """
        Module for test web_widget_x2many_2d_matrix""",

    'description': """
        You can test the web_widget_x2many_2d_matrix in the wizard in the menu of the parameter (testMatrix)
    """,

    'author': "e-COSI",
    'website': "http://www.e-cosi.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '10.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base','project','web_widget_x2many_2d_matrix'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
