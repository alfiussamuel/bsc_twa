# -*- coding: utf-8 -*-
# from odoo import http


# class TwaConvertCurrency(http.Controller):
#     @http.route('/twa_convert_currency/twa_convert_currency/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/twa_convert_currency/twa_convert_currency/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('twa_convert_currency.listing', {
#             'root': '/twa_convert_currency/twa_convert_currency',
#             'objects': http.request.env['twa_convert_currency.twa_convert_currency'].search([]),
#         })

#     @http.route('/twa_convert_currency/twa_convert_currency/objects/<model("twa_convert_currency.twa_convert_currency"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('twa_convert_currency.object', {
#             'object': obj
#         })
