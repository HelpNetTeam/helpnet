# -*- coding: utf-8 -*-
# from odoo import http


# class Helpnet(http.Controller):
#     @http.route('/helpnet/helpnet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/helpnet/helpnet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('helpnet.listing', {
#             'root': '/helpnet/helpnet',
#             'objects': http.request.env['helpnet.helpnet'].search([]),
#         })

#     @http.route('/helpnet/helpnet/objects/<model("helpnet.helpnet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('helpnet.object', {
#             'object': obj
#         })
