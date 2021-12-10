# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template"


    attachment = fields.Many2many('ir.attachment',
                                    string='Attachment',
                                    domain=[('res_model', '=', 'product.template')])
