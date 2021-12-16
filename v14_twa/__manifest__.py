# -*- coding: utf-8 -*-
{
    'name': "TWA CustomApps",

    'summary': """
        Custom Modul for TWA Projects""",

    'description': """
        BSC Custom Modul for TWA Odoo Implementation
    """,

    'author': "BSC Indonesia",
    'website': "https://bsc.co.id/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'version': '14.0.0.0',
    'category': 'Extra Tools',
    'sequence': 1,
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3', 

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sales.xml',
        'views/stock.xml',
        'report/invoice_report.xml',
        'report/invoice_template.xml',        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
