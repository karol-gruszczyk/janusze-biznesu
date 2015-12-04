from django.db import models
from apps.shares.models import Share, ShareGroup


class Correlation(models.Model):
    input_shares = models.ForeignKey(Share, related_name='+')
    output_share = models.ForeignKey(Share, related_name='+')
    day_interval = models.PositiveSmallIntegerField()
    value = models.FloatField()


class CorrelationSet(models.Model):
    name = models.CharField(max_length=32)
    shares = models.ManyToManyField(Share, related_name='+', blank=True)
    day_interval_start = models.SmallIntegerField()
    day_interval_end = models.SmallIntegerField()
    from_date = models.DateField()
