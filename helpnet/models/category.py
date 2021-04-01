from odoo import models, fields


class HelpnetCategory(models.Model):
    _name = 'helpnet.category'

    name = fields.Char()
    description = fields.Text()
