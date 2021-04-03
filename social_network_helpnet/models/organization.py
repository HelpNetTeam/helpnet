from odoo import models


class HelpnetProject(models.Model):
    _name = 'helpnet.project'
    _inherit = [
        'social_network.subscribe.mixin',
        'helpnet.project',
        ]