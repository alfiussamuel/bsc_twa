# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = "res.company"

    logo_so = fields.Binary('Logo Quotation')
    opening_report = fields.Text(
        default="Dear Mr./Mrs.,\n We thank you for your inquiry and we are pleased to offer you without engagement:"
    )
    term_condition_report = fields.Text(
        default="Price : Nett, Exclude PPN, Franco Purwakarta\n \
                Delivery : Indent 8-10 Weeks \n \
                Payment : 4 Weeks after delivery \n \
                Validity : 2 weeks"
    )
    closing_report =fields.Text(
        default="If you have any further questions, please do not hestitate to contact us again. We hope you will make use of this \n \
                advantageous offer and we look forward to receiving your firm order soon."
    )
