from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Property Types"
    _order = "name"
    
    name = fields.Char('Property Type', required=True)
    property_ids = fields.One2many("estate.property", "property_type_id")