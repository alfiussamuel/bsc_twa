from odoo import _, api, fields, models
from num2words import num2words

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    type = fields.Selection([
        ('local', 'Local'),
        ('import', 'Import'),
    ], string='Type', default='local')  

    @api.model
    def create(self, vals):
        if vals['type'] == 'local':
            vals['name'] = self.env['ir.sequence'].next_by_code('purchase.order.local')
        else:
            vals['name'] = self.env['ir.sequence'].next_by_code('purchase.order.import')
        return super(PurchaseOrder, self).create(vals)
    
    def num2word_po(self, amount_total, lang):
        words = num2words(round(amount_total), lang=lang).title()
        number_to_words = words.split('Koma',1)[0]
        res = number_to_words + " " + " Rupiah"
        return res

    # def write(self, vals):
    #     if 'type' in vals:
    #         if vals['type'] == 'local':
    #             vals['name'] = self.env['ir.sequence'].next_by_code('purchase.order.local')
    #         else:
    #             vals['name'] = self.env['ir.sequence'].next_by_code('purchase.order.import')
    #     return super(PurchaseOrder, self).write(vals)
