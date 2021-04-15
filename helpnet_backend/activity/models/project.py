from django.db import models


class Project(models.Model):

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    # organization_id = models.Many2one('helpnet.organization')
    # responsible_id = models.Many2one('res.partner')
    website = models.URLField()

    def __str__(self):
        return self.name
