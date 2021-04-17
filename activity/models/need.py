from django.db import models


class Need(models.Model):
    """Needs to be referenced in Activities (Referencial Table)"""

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()


class NeedUom(models.Model):
    """Unit of Measure for a Need"""

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
