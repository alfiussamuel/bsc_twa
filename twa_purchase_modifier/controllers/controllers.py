# -*- coding: utf-8 -*-
# from odoo import http


# class TwaPurchaseModifier(http.Controller):
#     @http.route('/twa_purchase_modifier/twa_purchase_modifier/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/twa_purchase_modifier/twa_purchase_modifier/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('twa_purchase_modifier.listing', {
#             'root': '/twa_purchase_modifier/twa_purchase_modifier',
#             'objects': http.request.env['twa_purchase_modifier.twa_purchase_modifier'].search([]),
#         })

#     @http.route('/twa_purchase_modifier/twa_purchase_modifier/objects/<model("twa_purchase_modifier.twa_purchase_modifier"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('twa_purchase_modifier.object', {
#             'object': obj
#         })
