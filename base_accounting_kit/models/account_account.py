# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2019-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

import time
from odoo import api, models, fields, _
from odoo.exceptions import UserError

# Export Product
class ExportProductLine(models.Model):
    _name = "export.product.line"

    reference = fields.Many2one('Reference')
    value = fields.Char('Value')
    
class ExportProduct(models.Model):
    _name = "export.product"

    product_template_id = fields.Char('Product External ID')
    product_id = fields.Char('Product ID')
    product_template_name = fields.Char('Product Name')
    attribute_id = fields.Char('Attribute')
    value_text = fields.Char(compute="_get_value_text", string="Values in Text")
    line_ids = fields.One2many('export.product.line', 'reference', 'Lines')

    @api.depends('line_ids.value')
    def _get_value_text(self):
        for res in self:
            value_text = ""
            if res.line_ids:
                for line in res.line_ids:
                    if not value_text:
                        value_text += line.value
                    elif value_text:
                        value_text += "," + line.value

            res.value_text = value_text
            
class CashFlow(models.Model):
    _inherit = 'account.account'

    def get_cash_flow_ids(self):
        cash_flow_id = self.env.ref('base_accounting_kit.account_financial_report_cash_flow0')
        if cash_flow_id:
            return [('parent_id.id', '=', cash_flow_id.id)]

    cash_flow_type = fields.Many2one('account.financial.report', string="Cash Flow type", domain=get_cash_flow_ids)

    @api.onchange('cash_flow_type')
    def onchange_cash_flow_type(self):
        for rec in self.cash_flow_type:
            # update new record
            rec.write({
                'account_ids': [(4, self._origin.id)]
            })

        if self._origin.cash_flow_type.ids:
            for rec in self._origin.cash_flow_type:
                # remove old record
                rec.write({'account_ids': [(3, self._origin.id)]})
