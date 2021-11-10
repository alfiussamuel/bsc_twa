# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template"


    margin = fields.Float('Margin (%)')
    type_product = fields.Char('Type')
    brand_product = fields.Char('Brand')

    @api.onchange('margin','standard_price')
    def onchange_persen_cost(self):
        if self.margin :
            if self.margin != 0 :
                cost = (self.margin /100) * self.standard_price

                self.list_price = cost + self.standard_price





