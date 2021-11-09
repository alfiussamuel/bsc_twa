# -*- coding: utf-8 -*-
# from odoo import http


# class V14Twa(http.Controller):
#     @http.route('/v14_twa/v14_twa/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/v14_twa/v14_twa/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('v14_twa.listing', {
#             'root': '/v14_twa/v14_twa',
#             'objects': http.request.env['v14_twa.v14_twa'].search([]),
#         })

#     @http.route('/v14_twa/v14_twa/objects/<model("v14_twa.v14_twa"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('v14_twa.object', {
#             'object': obj
#         })
