# -*- coding: utf-8 -*-
from odoo import http

# class BscFreightPurchase(http.Controller):
#     @http.route('/bsc_freight_purchase/bsc_freight_purchase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bsc_freight_purchase/bsc_freight_purchase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bsc_freight_purchase.listing', {
#             'root': '/bsc_freight_purchase/bsc_freight_purchase',
#             'objects': http.request.env['bsc_freight_purchase.bsc_freight_purchase'].search([]),
#         })

#     @http.route('/bsc_freight_purchase/bsc_freight_purchase/objects/<model("bsc_freight_purchase.bsc_freight_purchase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bsc_freight_purchase.object', {
#             'object': obj
#         })