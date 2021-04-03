from odoo import models


class HelpnetOrganization(models.Model):
    _name = 'helpnet.organization'
    _inherit = [
        'social_network.subscribe.mixin',
        'helpnet.organization',
        ]