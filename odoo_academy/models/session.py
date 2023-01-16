from odoo import api, fields, models

class Session(models.Model):
    _name = 'academy.session'
    _description = 'Session Info'

    course_id = fields.Many2one("academy.course", ondelete='cascade', required=True)
    name = fields.Char("Title", related='course_id.name')
    instructor_id = fields.Many2one("res.partner")
    student_ids = fields.Many2many("res.partner")