from odoo import api, fields, models, exceptions
from datetime import timedelta #hacer sin este import

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property Offers"
    _order = "price desc"
    
    price = fields.Float()
    status = fields.Selection(
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    create_date = fields.Date(copy=False, default=lambda self: fields.Date.today())
    date_deadline = fields.Date('Deadline', compute="_compute_deadline")
    validity = fields.Integer(default=7)

    @api.depends("create_date", "validity")
    def _compute_deadline(self):
        for record in self:
                record.date_deadline = record.create_date + timedelta(days=record.validity)

    #hacer inverse should be easy now

    def action_accept(self):
        for record in self:
            for i in record.property_id.offer_id.mapped('status'):
                if i == 'accepted':
                    raise exceptions.UserError('Theres an accepted offer already')
                    return True
            record.status = 'accepted'
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id
            record.property_id.state = 'oaccepted'
        return True

    def action_refuse(self):
        for record in self:
            record.status = 'refused'
            record.property_id.selling_price = 0
            record.property_id.buyer_id = ''
        return True