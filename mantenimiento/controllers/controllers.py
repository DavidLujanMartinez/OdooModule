# -*- coding: utf-8 -*-
# from odoo import http


# class Mantenimiento(http.Controller):
#     @http.route('/mantenimiento/mantenimiento/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mantenimiento/mantenimiento/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mantenimiento.listing', {
#             'root': '/mantenimiento/mantenimiento',
#             'objects': http.request.env['mantenimiento.mantenimiento'].search([]),
#         })

#     @http.route('/mantenimiento/mantenimiento/objects/<model("mantenimiento.mantenimiento"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mantenimiento.object', {
#             'object': obj
#         })
