from odoo import api, fields, models, exceptions

class Course(models.Model):
    _name = 'academy.course'
    _description = 'Course Info'

    name = fields.Char('Title', required=True)
    description = fields.Text('Description')
    active = fields.Boolean()
    base_price = fields.Float('Base Price', default=0.00)
    additional_fee = fields.Float('Additional Fee', default=10.00)
    total_price = fields.Float('Total Price', readonly=True, store=True) #no se guarda, usar  force_save="1" en el field
    session_ids = fields.One2many('academy.session', 'course_id')
    level = fields.Selection(selection=[('beginner', 'Beginner'),
                                        ('intermediate', 'Intermediate'),
                                        ('advanced', 'Advanced')], copy=False)
    
    @api.onchange('base_price', 'additional_fee')
    def _onchange_total(self):
        if self.base_price < 0.00:
            raise exceptions.UserError('Base Price cannot be negative')
        self.total_price = self.base_price + self.additional_fee

    @api.constrains('additional_fee')
    def _check_add_fee(self):
        for record in self:
            if record.additional_fee < 10.00:
                raise exceptions.ValidationError('Additional Fee cannot be less than 10.00: %s' % record.additional_fee)