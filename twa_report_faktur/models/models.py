from odoo import _, api, fields, models
from num2words import num2words

class AccountMove(models.Model):
    _inherit = 'account.move'

    berita_acara = fields.Char('Berita Acara')
    amount_words = fields.Char(compute='_compute_amount_words', string='Amount Words')
    signed_partner_id = fields.Many2one('res.partner', string='Signed By')
    payment_journal_id = fields.Many2one('account.journal', string='Payment Journal', domain=[('type','=','bank')])
    ppn_msg = fields.Text('PPN Message')

    @api.depends('amount_total')
    def _compute_amount_words(self):
        for rec in self:
            if rec.amount_total:
                rec.amount_words = (num2words(rec.amount_total,lang='id') + ' ' + (self.currency_id.currency_unit_label or '')).upper()