from odoo import _, api, fields, models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    type = fields.Selection([
        ('local', 'Local'),
        ('import', 'Import'),
    ], string='Type', default='local')  

    @api.model
    def create(self, vals):
        if vals['type'] == 'local':
            vals['name'] = self.env['ir.sequence'].next_by_code('purchase.order.local')
        else:
            vals['name'] = self.env['ir.sequence'].next_by_code('purchase.order.import')
        return super(PurchaseOrder, self).create(vals)

    # def write(self, vals):
    #     if 'type' in vals:
    #         if vals['type'] == 'local':
    #             vals['name'] = self.env['ir.sequence'].next_by_code('purchase.order.local')
    #         else:
    #             vals['name'] = self.env['ir.sequence'].next_by_code('purchase.order.import')
    #     return super(PurchaseOrder, self).write(vals)
