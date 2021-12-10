# -*- coding: utf-8 -*-
{
    'name': "Sale Order Report",
    'summary': """Report Sale Order""",
    'description': "Report Sale Order",
    'category': 'Sales',
    'version': '14.0.1.0.0',
    'depends': ['sale'],
    'data': [
        'views/res_partner_view.xml',
        'views/res_company_view.xml',
        'views/sale_order_view.xml',
        'report/quotation_report.xml'
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
