from odoo import api, fields, models

class Course(models.Model):
	_name = 'academy.course'
	_description = 'Course Info'

	name = fields.Char('Title', required=True)
	description = fields.Text('Description')
	active = fields.Boolean()

	level = fields.Selection(selection=[('beginner', 'Beginner'),
				   						('intermediate', 'Intermediate'),
				   						('advanced', 'Advanced')], copy=False)
