# -*- coding: utf-8 -*-
{
    'name': "Purchase Module Modifier For TWA",

    'summary': """
        This module to modify purchase odoo modules.""",

    'description': """
        This module to modify purchase odoo modules.
    """,

    'author': "PT. BSC Indonesia",
    'website': "http://www.bsc.co.id",
    'category': 'Inventory',
    'version': '0.1',
    'depends': ['base', 'purchase', 'purchase_stock', 'purchase_discount'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/purchase_order.xml',
        'views/sequence.xml',
        'views/report_purchaseorder.xml',
    ],
}
