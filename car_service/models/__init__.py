from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class CarService(models.Model):
    _name = 'car.service'
    _description = 'Car Service'

    name = fields.Char(string='Name')
    owner_id = fields.Many2one('res.partner', string='Owner')
    service_id = fields.Many2one('service', string='')

class Service(models.Model):
    _name = 'service'
    _description = "Services"

    name = fields.Char(string='Name')