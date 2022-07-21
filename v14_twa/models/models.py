from odoo import models, fields, api
from datetime import datetime
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    company_selection = fields.Selection(
        [('TWA', 'TWA'),
         ('BSM', 'BSM'),('KP', 'KP')],
        'Company', default='TWA')

    # @api.model
    # def create(self, vals):

    #     # Custom Format nomor invoice yang berbeda untuk tiap company selection
    #     # INV/TWA/YYYY/MM/001
    #     # INV/BSM/YYYY/MM/001
    #     # INV/KP/YYYY/MM/001

    #     sequence = self.env['ir.sequence'].next_by_code('sale.order.custom')
    #     inv_seq = 'INV/'+vals['company_selection']+'/'+str(datetime.now().year)+'/'+str(datetime.now().month)+'/'+str(sequence)
    #     vals['name'] = inv_seq or _('New')
    #     result = super(SaleOrder, self).create(vals)
    #     return result   

    # sale.advance.payment.inv


class AccountMove(models.Model):
    _inherit = 'account.move'

    company_selection = fields.Selection(
        [('TWA', 'TWA'),
         ('BSM', 'BSM'),('KP', 'KP')],
        'Company', default='TWA')

    # @api.model
    # def create(self, vals_list):
    #     company = "TWA"
    #     # Custom Format nomor invoice yang berbeda untuk tiap company selection
    #     # INV/TWA/YYYY/MM/001
    #     # INV/BSM/YYYY/MM/001
    #     # INV/KP/YYYY/MM/001

    #     # sequence = self.env['ir.sequence'].next_by_code('sale.order.custom')
    #     # last_seq = self._get_last_sequence(relaxed=True)
    #     _logger.warning(str(vals_list))

    #     print (vals_list)
    #     # if vals_list['invoice_origin']:
    #     #     company = self.env['sale.order'].search([('name','=',vals_list['invoice_origin'])]).company_selection
    #     # elif not vals_list['invoice_origin']:
    #     # if vals_list['company_selection']:
    #     #     company = vals_list['company_selection']

    #     print ("Vals List ", vals_list)
    #     if vals_list.get('partner_id'):
    #         sequence = self.env['ir.sequence'].next_by_code('account.invoice.custom')
    #         inv_seq = 'INV/' + str(company) + '/' + str(datetime.now().year) + '/' + str(datetime.now().month) + '/' + str(sequence)
    #         vals_list['name'] = inv_seq or _('New')
        
    #     result = super(AccountMove, self).create(vals_list)
    #     print ("Name 2 ", result.name)
    #     return result


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    company_selection = fields.Selection(
        [('TWA', 'TWA'),
         ('BSM', 'BSM'),('KP', 'KP')],
        'Company', default='TWA')

    # @api.model
    # def create(self, vals_list):
    #     _logger.warning(str(vals_list))
    #     if vals_list['origin'] :
    #         company = self.env['sale.order'].search([('name','=',vals_list['origin'])]).company_selection
    #         _logger.warning(str(company))
    #         vals_list['company_selection'] = company
    #     result = super(StockPicking, self).create(vals_list)
    #     return result              