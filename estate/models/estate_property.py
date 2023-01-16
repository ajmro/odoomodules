from odoo import api, fields, models, exceptions


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estates properties"
    _order = "expected_price desc"
    
    name = fields.Char('Title', required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=lambda self: fields.Date.today()) #should be 3 months from today desu
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer('Living Area (sqm)')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer('Garden Area (sqm)')
    #active = fields.Boolean(default=False)
    property_type_id = fields.Many2one("estate.property.type")
    salesperson_id = fields.Many2one("res.users", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", copy=False)
    tags_id = fields.Many2many("estate.property.tag")
    offer_id = fields.One2many("estate.property.offer", "property_id")
    total_area = fields.Integer(compute="_compute_total")
    best_price = fields.Float(compute="_compute_bestprice")
    state = fields.Selection(
        selection=[('new', 'New'), ('oreceived', 'Offer Received'), ('oaccepted', 'Offer Accepted'), ('sold', 'Sold'),
        ('canceled', 'Canceled')], required=True, copy=False, default='new')
    garden_orientation = fields.Selection(
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])



    #agregar constrains sql para validar datos

    @api.constrains('selling_price') #usar metodos float
    def check_selling_price(self):
        for record in self:
            if int(record.selling_price) != 0:
                if int(record.selling_price) < int((record.expected_price * 90)/100):
                    raise exceptions.ValidationError('Selling price cannot be lower than 90% of the expected price')

    @api.depends('garden_area', 'living_area')
    def _compute_total(self):
        for record in self:
            record.total_area = record.garden_area + record.living_area


    @api.depends('offer_id')
    def _compute_bestprice(self):
        for record in self:
            try:
                record.best_price = max(record.offer_id.mapped('price'))
            except:
                record.best_price = 0


    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden == True:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = ''

    def action_sold(self):
        for record in self:
            if record.state == 'canceled':
                raise exceptions.UserError('Canceled properties cannot be sold.')
                return True
            record.state = "sold"
        return True


    def action_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise exceptions.UserError('Sold properties cannot be canceled.')
                return True
            record.state = "canceled"
        return True