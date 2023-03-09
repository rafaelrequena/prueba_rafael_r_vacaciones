# -*- coding: utf-8 -*-

from odoo import models, fields, api, _




class HrEmployeeHolidaysLeave(models.Model):
    _name = 'hr.employee.holidays.leave'
    _description = 'Hr Employee Holidays Leave'
    _rec_name = 'employee_id'

    @api.depends('company_id')
    def _compute_company_id(self):
        for rec in self:
            rec.company_id = self.env.company


    employee_id = fields.Many2one('hr.employee', string='Employee')
    date_start = fields.Date(string='Date Start')
    date_end = fields.Date(string='Date End')
    company_id = fields.Many2one(comodel_name='res.company', string='Company',
                                store=True, readonly=True,
                                compute='_compute_company_id')
    user_approved_id = fields.Many2one('res.users', string='User Approved')
    
    state = fields.Selection([
        ('unresolved', 'Unresolved'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='state', default='unresolved')


    def approved_request(self):
        for rec in self:
            rec.write({'state': 'approved','user_approved_id': self.env.user.id})

    def rejected_request(self):
        for rec in self:
            rec.write({'state': 'rejected'})



