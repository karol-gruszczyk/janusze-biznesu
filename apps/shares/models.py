from django.db import models


class Share(models.Model):
    name = models.CharField(max_length=32)
    updated_daily = models.BooleanField(null=False)


class ShareRecord(models.Model):
    share = models.ForeignKey(Share)
    date = models.DateField(null=False)
    open = models.FloatField()
    close = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    volume = models.FloatField()


class ShareGroup(models.Model):
    relation = models.ManyToManyField(Share)
