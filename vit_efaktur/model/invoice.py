from odoo import api, fields, models, _

class AccountMove(models.Model):
    _name = 'account.move'
    _inherit = 'account.move'

    efaktur_id  = fields.Many2one(comodel_name="vit.efaktur", string="Faktur Pajak", required=False, )
    is_efaktur_exported = fields.Boolean(string="Is eFaktur Exported",  )
    date_efaktur_exported = fields.Datetime(string="eFaktur Exported Date", required=False, )

    # masa_pajak = fields.Char(string="Masa Pajak", required=False, compute="_masa_pajak" )
    # tahun_pajak = fields.Char(string="Tahun Pajak", required=False, compute="_tahun_pajak")

    masa_pajak = fields.Char(string="Masa Pajak", required=False)
    tahun_pajak = fields.Char(string="Tahun Pajak", required=False)

    efaktur_masukan = fields.Char(string="Nomor Seri Faktur Pajak", required=False, )
    is_berikat = fields.Boolean(string="Kawasan Berikat?", related="partner_id.is_berikat" )
    prefix_berikat = fields.Char(string="Prefix NSFP", compute="_get_prefix_berikat" )

    @api.depends("is_berikat")
    def _get_prefix_berikat(self):
        for rec in self:
            if rec.is_berikat:
                rec.prefix_berikat = '070'
            else:
                rec.prefix_berikat = ''

    # @api.depends("invoice_date")
    # def _masa_pajak(self):
    #     for inv in self:
    #         if inv.invoice_date:
    #             d = inv.invoice_date.month
    #             # d = inv.invoice_date.split("-")
    #             inv.masa_pajak = str(d)

    # @api.depends("invoice_date")
    # def _tahun_pajak(self):
    #     for inv in self:
    #         if inv.invoice_date:
    #             d = inv.invoice_date.year
    #             # d = inv.invoice_date.split("-")
    #             inv.tahun_pajak = str(d)

    # @api.multi
    def action_invoice_open(self):
        res = super(invoice, self).action_invoice_open()
        if self:
            self.is_efaktur_exported=False
        return res
