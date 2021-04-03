from odoo import models, fields


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = [
        'social_network.subscribe.mixin',
        'res.partner',
        ]

    subscriber_ids = fields.Many2many(
        comodel='res.partner',
        relation='partner_subscriber',
        column1='subscriber_id', 
        column2='subscription_dest', 
        )