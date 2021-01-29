from odoo import models, fields


class HelpnetProject(models.Model):
    _name = 'helpnet.project'

    name = fields.Char()
    organization_id = fields.Many2one('helpnet.organization')
    responsible_id = fields.Many2one('res.partner')
    website = fields.Char()
