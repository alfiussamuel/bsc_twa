# -*- coding: utf-8 -*-

from odoo import api, fields, models

class StockLandedCost(models.Model):
    _inherit = 'stock.landed.cost'

    avg_landed_cost_lines = fields.One2many('average.landed.cost.lines',
                                            'line_id', string='Order Lines')

    def button_validate(self):
        res = super(StockLandedCost, self).button_validate()
        for line in self.avg_landed_cost_lines:
            has_val = False
            moves = self.picking_ids.mapped('move_ids_without_package')
            fifo = self.env['stock.valuation.layer'].search([('product_id','=',line.product_id.id), ('remaining_qty','>',0)], order='create_date asc', limit=1)
            for move in moves:
                for val in move.stock_valuation_layer_ids.filtered(lambda x: x.product_id.id == line.product_id.id and x.remaining_qty > 0):
                    has_val = True
                    values = val.unit_cost + line.average_landed_cost
                    val.unit_cost = values
                    val.value = values * val.quantity
                    if val.id == fifo.id:
                        line.product_id.standard_price = values

            if has_val:
                self.sudo().stock_valuation_layer_ids.unlink()
            # line.product_id.standard_price += line.average_landed_cost
        return res

    def compute_average_landed_cost(self):
        AverageLandedCostLines = self.env['average.landed.cost.lines']
        AverageLandedCostLines.search([('line_id', 'in', self.ids)]).unlink()
        for line in self.valuation_adjustment_lines:
            data = self.avg_landed_cost_lines.filtered(lambda t: t.line_id.id == line.cost_id.id)
            if not data:
                self.avg_landed_cost_lines.create({
                    'product_id': line.product_id.id,
                    'quantity': line.quantity,
                    'additional_landed_cost_sum': line.additional_landed_cost,
                    'average_landed_cost': line.additional_landed_cost / line.quantity,
                    'line_id': self.id
                })
            else:
                val = self.avg_landed_cost_lines.filtered(
                    lambda t: t.line_id.id == line.cost_id.id and t.product_id.id == line.product_id.id)
                if val:
                    val.additional_landed_cost_sum += line.additional_landed_cost
                    val.average_landed_cost = val.additional_landed_cost_sum / line.quantity
                else:
                    self.avg_landed_cost_lines.create({
                        'product_id': line.product_id.id,
                        'quantity': line.quantity,
                        'additional_landed_cost_sum': line.additional_landed_cost,
                        'average_landed_cost': line.additional_landed_cost / line.quantity,
                        'line_id': self.id
                    })


class AverageLandedCostLines(models.Model):
    _name = 'average.landed.cost.lines'
    _description = 'Average Landed cost Lines'

    line_id = fields.Many2one('stock.landed.cost')
    product_id = fields.Many2one('product.product', 'Product', required=True)
    quantity = fields.Integer('Quantity')
    additional_landed_cost_sum = fields.Float('Sum')
    average_landed_cost = fields.Float('Average Landed Cost')
