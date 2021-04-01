from odoo import api, fields, models


class SocialNetworkPost(models.Model):
    _name = 'social_network.post'

    name = fields.Char()
    user_id = fields.Many2one('res.users')
    date = fields.Datetime
    body = fields.Html()
    like_ids = fields.One2many('social_network.like', 'post_id')
    like_count = fields.Integer(compute='_like_count')
    comment_ids = fields.One2many('social_network.post.comment', 'post_id')
    share_count = fields.Integer()
    image_ids = fields.Many2many('ir.attachment')

    def _like_count(self):
        for rec in self:
            rec.likes_count = len(rec.like_ids)
    
    def _add_share(self):
        """Increase by one the Share Count when an user shares a post"""
        for rec in self:
            rec.share_count += 1


class SocialNetworkPostComment(models.Model):
    _name = 'social_network.post.comment'
    _rec_name = 'date'
    _order = 'date desc'

    body = fields.Html()
    date = fields.Datetime()
    user_id = fields.Many2one('res.users')
    post_id = fields.Many2one('social_network.post')
    like_ids = fields.One2many('social_network.like', 'comment_id')
    like_count = fields.Integer(compute='_like_count')
    # comment_ids = fields.Many2many('social_network.post.comment', help='Replies') TODO

    def _like_count(self):
        for rec in self:
            rec.likes_count = len(rec.like_ids)

class SocialNetworkLike(models.Model):
    _name = 'social_network.like'
    _rec_name = 'date'

    user_id = fields.Many2one('res.users')
    post_id = fields.Many2one('social_network.post')
    comment_id = fields.Many2one('social_network.comment')
    date = fields.Datetime()