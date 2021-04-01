from odoo import models, fields


class HelpnetOrganization(models.Model):
    _name = 'helpnet.organization'

    name = fields.Char()
    responsible_id = fields.Many2one('res.partner')
    website = fields.Char()
