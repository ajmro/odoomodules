from odoo import fields, models

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Property Tags"
    _order = "name"
    
    name = fields.Char('Property Tags', required=True)
    color = fields.Integer()