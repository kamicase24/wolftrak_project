# -*- coding: utf-8 -*-
from odoo import http

# class WolftrakProject(http.Controller):
#     @http.route('/wolftrak_project/wolftrak_project/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wolftrak_project/wolftrak_project/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wolftrak_project.listing', {
#             'root': '/wolftrak_project/wolftrak_project',
#             'objects': http.request.env['wolftrak_project.wolftrak_project'].search([]),
#         })

#     @http.route('/wolftrak_project/wolftrak_project/objects/<model("wolftrak_project.wolftrak_project"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wolftrak_project.object', {
#             'object': obj
#         })