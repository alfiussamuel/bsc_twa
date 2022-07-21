# -*- coding: utf-8 -*-
{
    'name': "Convert Currency",

    'summary': """
        Convert Currency in PO and SO""",

    'description': """
        Convert Currency in PO and SO
    """,

    'author': "PT. BSC Indonesia",
    'website': "http://www.bsc.co.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_currency_rate_views.xml',
        'views/sale_order_views.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "application": True,
}
