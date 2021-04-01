from odoo import models, fields


class HelpnetTag(models.Model):
    _name = 'helpnet.tag'

    name = fields.Char()
    description = fields.Text()
