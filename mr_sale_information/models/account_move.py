# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class AccountMove(models.Model):
    _inherit = "account.move"

    mr_so_id = fields.Many2one('sale.order', string='Sale Order')
