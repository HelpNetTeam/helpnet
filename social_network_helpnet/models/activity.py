from odoo import models


class HelpnetActivity(models.Model):
    _name = 'helpnet.activity'
    _inherit = [
        'social_network.subscribe.mixin',
        'helpnet.activity',
        ]