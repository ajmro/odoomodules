from odoo import api, fields, models, exceptions

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_session_product = fields.Boolean('Use as session product', help='Check to use this as a Product for Session Fee', default=False)
    