from odoo import models, fields


class HelpnetNeed(models.Model):
    _name = 'helpnet.need'

    name = fields.Char()
    description = fields.Text()


class HelpnetNeedUom(models.Model):
    _name = 'helpnet.need.uom'

    name = fields.Char()
    description = fields.Text()
