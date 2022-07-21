from odoo import _, api, fields, models
from odoo.tools import float_is_zero


class ResCurrencyRate(models.Model):
    _inherit = 'res.currency.rate'
    
    start_date = fields.Date('Start Date')  
    actual_rate = fields.Float('Actual Rate')
    
    @api.onchange('actual_rate')
    def _onchange_actual_rate(self):
        if not float_is_zero(self.actual_rate,precision_digits=2):
            self.rate = 1 / self.actual_rate 