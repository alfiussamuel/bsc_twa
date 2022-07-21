from odoo import _, api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    backdate_order = fields.Date('Backdate Order')

    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        res['currency_id'] = self.env.company.currency_id.id
        return res


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    def _prepare_invoice_line(self, **optional_values):
        res = super(SaleOrderLine, self)._prepare_invoice_line(**optional_values)
        date_order = self.order_id.date_order.date() if not self.order_id.backdate_order else self.order_id.backdate_order
        date = self.order_id.date_order.date() if not self.order_id.backdate_order else self.order_id.backdate_order
        currency_id = self.env.company.currency_id
        rates = self.env['res.currency.rate'].search([('currency_id', '=', self.order_id.currency_id.id)]).filtered(lambda x : x.name.year == date_order.year)        
        
        for this in rates:
            if this.start_date:
                if date_order >= this.start_date and date_order <= this.name :
                    date = this.name
            else:
                raise ValueError("Start Date in Rates is null")
            
        res['price_unit'] = self.currency_id._convert(self.price_unit,currency_id, self.company_id, date, round=False)
        
        
        return res        