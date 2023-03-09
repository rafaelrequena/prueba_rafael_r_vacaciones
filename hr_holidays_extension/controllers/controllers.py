# -*- coding: utf-8 -*-
# from odoo import http


# class HrHodidaysExtension(http.Controller):
#     @http.route('/hr_hodidays_extension/hr_hodidays_extension', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_hodidays_extension/hr_hodidays_extension/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_hodidays_extension.listing', {
#             'root': '/hr_hodidays_extension/hr_hodidays_extension',
#             'objects': http.request.env['hr_hodidays_extension.hr_hodidays_extension'].search([]),
#         })

#     @http.route('/hr_hodidays_extension/hr_hodidays_extension/objects/<model("hr_hodidays_extension.hr_hodidays_extension"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_hodidays_extension.object', {
#             'object': obj
#         })
