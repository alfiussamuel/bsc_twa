# -*- coding: utf-8 -*-
{
    'name': 'Landed Cost Based Percentase',
    'version': '10',
    'category': 'Custom',
    'author': 'BSC',

    # any module necessary for this one to work correctly
    'depends': ['stock_landed_costs','product','purchase'],

    # always loaded
    'data': [
                'views/landedcost_view.xml',
                'views/product_view.xml'
            ],

}
