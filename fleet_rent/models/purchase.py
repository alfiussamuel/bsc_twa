# See LICENSE file for full copyright and licensing details.
"""Fleet Tenant, Res Partner Model."""

import re
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    installment_type = fields.Selection([
        ('Flat','Flat'),
        ('Floating','Floating')
    ], default="Flat", string="Installment Type")
    leasing_id = fields.Many2one('res.partner', string="Leasing")
    global_discount = fields.Float('Discount')
    
    def action_calculate_leasing(self):
        for res in self:
            for line in res.order_line:
                if line.leasing_ids:
                    for leasing in line.leasing_ids:
                        leasing.unlink()

                number = 1
                tenor = line.tenor
                amount_base = (line.price_unit - line.down_payment) / line.tenor
                amount_interest = line.amount_interest * amount_base / 100
               
                while tenor > 0:
                    self.env['purchase.order.line.leasing'].create({
                        'reference': line.id,
                        'number': number,
                        'amount_base': amount_base,
                        'amount_interest': amount_interest,
                        'amount_total': (amount_base + amount_interest)
                    })

                    number = number + 1
                    tenor = tenor - 1

            return True

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    year = fields.Integer('Year')
    color = fields.Many2one('color.color', string='Color')
    brand_id = fields.Many2one('fleet.vehicle.model.brand', string='Brand')
    model_id = fields.Many2one('fleet.vehicle.model', string='Model')
    amount_interest = fields.Float('Bunga')
    tenor = fields.Integer('Tenor')
    leasing_ids = fields.One2many('purchase.order.line.leasing', 'reference', string='Leasing')
    down_payment = fields.Float('Down Payment')

class PurchaseOrderLineLeasing(models.Model):
    _name = "purchase.order.line.leasing"

    reference = fields.Many2one('purchase.order.line', string="Purchase Order")
    number = fields.Char('Number')
    amount_base = fields.Float('Nilai Pokok')
    amount_interest = fields.Float('Bunga')
    amount_total = fields.Float('Nilai Cicilan')
    state = fields.Selection([
        ('Unpaid','Unpaid'),
        ('Paid','Paid')
    ], default='Unpaid', string="Status")

    def action_create_payment(self):
        return True
