from odoo import api, fields, models


class socialNetworkSubscribeMixin(models.AbstractModel):
    _name = 'social_network.subscribe.mixin'

    subscriber_ids = fields.Many2many('res.partner')
    user_subscribed = fields.Boolean(compute='_compute_user_subscribed')

    def action_toggle_subscribe_user(self):
        """Susbcribe the logged user to receive further notifications"""
        partner_id = self.env.user.partner_id.id
        for rec in self:
            if partner_id not in rec.subscriber_ids.ids:
                rec.write({'subscriber_ids': [(4, partner_id)]})
            else:
                rec.write({'subscriber_ids': [(3, partner_id)]})
    
    @api.depends('subscriber_ids')
    def _compute_user_subscribed(self):
        """Find out if the logged user is subscribed.
        This is meant for showing/hiding the Subscribe/Unsubscribe
        button in the form view"""
        partner_id = self.env.user.partner_id.id
        for rec in self:
            if partner_id in rec.subscriber_ids.ids:
                rec.user_subscribed = True
            else:
                rec.user_subscribed = False
        return True