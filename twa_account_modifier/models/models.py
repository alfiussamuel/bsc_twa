from odoo import _, api, fields, models

class AccountBankStatement(models.Model):
    _inherit = 'account.bank.statement'

    sale_order_ref = fields.Char('Sales Order Reference')

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    analytic_account_id = fields.Many2one('account.analytic.account', string='Analytic Account')    