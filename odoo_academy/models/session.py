from odoo import api, fields, models
from datetime import timedelta

class Session(models.Model):
    _name = 'academy.session'
    _description = 'Session Info'

    course_id = fields.Many2one("academy.course", ondelete='cascade', required=True)
    name = fields.Char("Title", related='course_id.name')
    instructor_id = fields.Many2one("res.partner")
    student_ids = fields.Many2many("res.partner")
    #create_date = fields.Date(copy=False, default=lambda self: fields.Date.today())
    start_date = fields.Date(default=fields.Date.today())
    duration = fields.Integer('Session Days', default=1)
    end_date = fields.Date('End Date', compute='_compute_end_date', inverse='_inverse_end_date', store=True)
    total_price = fields.Float('Total Price', related='course_id.total_price')

    @api.depends("start_date", "duration")
    def _compute_end_date(self):
        for record in self:
            if not (record.start_date and record.duration):
                record.end_date = record.start_date
            else:
                record.end_date = record.start_date + timedelta(days=record.duration)

    def _inverse_end_date(self):
        for record in self:
            if record.start_date and record.end_date:
                record.duration = (record.end_date - record.start_date).days + 1
            else:
                continue

