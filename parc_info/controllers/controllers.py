# -*- coding: utf-8 -*-
# from odoo import http


# class ParcInfo(http.Controller):
#     @http.route('/parc_info/parc_info/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/parc_info/parc_info/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('parc_info.listing', {
#             'root': '/parc_info/parc_info',
#             'objects': http.request.env['parc_info.parc_info'].search([]),
#         })

#     @http.route('/parc_info/parc_info/objects/<model("parc_info.parc_info"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('parc_info.object', {
#             'object': obj
#         })
