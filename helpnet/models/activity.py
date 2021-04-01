# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HelpnetActivity(models.Model):
    _name = 'helpnet.activity'
    _description = 'Helpnet Activity'

    name = fields.Char()
    organization_id = fields.Many2one('helpnet.organization')
    project_id = fields.Many2one('helpnet.project')
    date = fields.Datetime()
    latitude = fields.Float()
    longitude = fields.Float()
    category_id = fields.Many2one('helpnet.category', 'Category')
    # age_rating_id = fields.Many2one('helpnet.activity.age_rating')
    need_ids = fields.One2many('helpnet.activity.need', 'activity_id')
    tag_ids = fields.Many2many('helpnet.tag')
    comment_ids = fields.One2many('helpnet.activity.comment', 'activity_id')
    rating_ids = fields.One2many('helpnet.activity.rating', 'activity_id')


class HelpnetActivityNeed(models.Model):
    _name = 'helpnet.activity.need'
    _rec_name = 'need_id'

    need_id = fields.Many2one('helpnet.need')
    uom_id = fields.Many2one('helpnet.need.uom')
    amount = fields.Float()
    activity_id = fields.Many2one('helpnet.activity')


class HelpnetActivityComment(models.Model):
    _name = 'helpnet.activity.comment'
    _rec_name = 'comment'

    comment = fields.Text()
    partner_id = fields.Many2one('res.partner')
    activity_id = fields.Many2one('helpnet.activity')


class HelpnetActivityRating(models.Model):
    _name = 'helpnet.activity.rating'
    _rec_name = 'rating'

    rating = fields.Selection([('1', 'Bad'),
                               ('2', 'Kinda Bad'),
                               ('3', 'Normal'),
                               ('4', 'Great'),
                               ('5', 'Excellent')])
    partner_id = fields.Many2one('res.partner')
    activity_id = fields.Many2one('helpnet.activity')



#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
