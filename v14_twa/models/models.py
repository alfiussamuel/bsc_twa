from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    company_selection = fields.Selection(
        [('TWA', 'TWA'),
         ('BSM', 'BSM'),('KP', 'KP')],
        'Company')