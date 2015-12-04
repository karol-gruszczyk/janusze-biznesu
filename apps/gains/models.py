from django.db import models
from apps.shares.models import Share, ShareRecord


class Gain(models.Model):
    share = models.ForeignKey(Share, related_name='gains')
    date = models.DateField(db_index=True)
    lower_record = models.OneToOneField(ShareRecord, related_name='upper_gain')
    upper_record = models.OneToOneField(ShareRecord, related_name='lower_gain')
    volume_gain = models.FloatField()
    open_gain = models.FloatField()
    close_gain = models.FloatField()
    high_gain = models.FloatField()
    low_gain = models.FloatField()

    class Meta:
        index_together = ['share', 'date']
        ordering = ['lower_record']
