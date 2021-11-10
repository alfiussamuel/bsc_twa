# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': "Sale Information",
    'description': """
        - Add SO Field on Stock Picking.
        - Add SO Field on Account Move.
    """,

    'author': "Mochamad Rezki",
    'website': "https://www.linkedin.com/in/mochamad-rezki/",
    'license': "AGPL-3",

    'category': 'Stock',
    'version': '14.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['account', 'sale', 'stock'],

    # always loaded
    'data': [
        'views/account_move_views.xml',
        'views/stock_picking_views.xml',
    ],
    'installable': True,
}
