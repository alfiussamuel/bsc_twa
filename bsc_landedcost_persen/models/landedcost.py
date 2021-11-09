# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockLandedCostLine(models.Model):
    _inherit = "stock.landed.cost.lines"


    persen_cost = fields.Float('Cost (%)')


    @api.onchange('product_id')
    def onchange_product_id(self):
        self.name = self.product_id.name or ''
        self.split_method = self.product_id.product_tmpl_id.split_method_landed_cost or self.split_method or 'equal'
        accounts_data = self.product_id.product_tmpl_id.get_product_accounts()
        self.account_id = accounts_data['stock_input']

    @api.onchange('persen_cost','vendor_bill_id')
    def onchange_persen_cost(self):
        if self.cost_id.vendor_bill_id :
            if self.persen_cost != 0 :
                cost = (self.persen_cost /100) * self.cost_id.vendor_bill_id.amount_total

                self.price_unit = cost

            else :
                self.price_unit = 0.0





