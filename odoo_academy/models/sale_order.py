from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'Session Info'

    session_id = fields.Many2one("academy.session", string='Related Session', ondelete='set null')
    instructor_id = fields.Many2one(string='Session Instructor', related='session_id.instructor_id') #check related parameter!
    student_ids = fields.Many2many(string='Students', related='session_id.student_ids')
