# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    opening_report = fields.Text(default=lambda self: self.env.company.opening_report)
    term_condition_report = fields.Text(default=lambda self: self.env.company.term_condition_report)
    closing_report =fields.Text(default=lambda self: self.env.company.closing_report)
