from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    
    
    def _prepare_invoice(self):
        res = super(PurchaseOrder, self)._prepare_invoice()
        res["currency_id"] = self.env.company.currency_id.id
        return res    

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    
    def _prepare_account_move_line(self, move=False):
        res = super(PurchaseOrderLine, self)._prepare_account_move_line(move)
        date_order = self.order_id.date_order 
        date = self.order_id.date_order.date()
        currency_id = self.env.company.currency_id
        rates = self.env['res.currency.rate'].search([('currency_id', '=', self.order_id.currency_id.id)]).filtered(lambda x : x.name.year == date_order.year)        
        
        for this in rates:
            if this.start_date:
                if date_order.date() >= this.start_date and date_order.date() <= this.name :
                    date = this.name
            else:
                raise ValueError("Start Date in Rates is null")
                
        res['price_unit'] = self.currency_id._convert(self.price_unit,currency_id, self.company_id, date, round=False)
        
        
        return res    
    
