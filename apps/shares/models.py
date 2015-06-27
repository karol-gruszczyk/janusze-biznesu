from django.db import models


class Share(models.Model):
    name = models.CharField(max_length=32)
    visible_name = models.CharField(max_length=64, null=True)
    updated_daily = models.BooleanField(default=False)

    def __str__(self):
        return self.visible_name if self.visible_name else self.name


class ShareRecord(models.Model):
    share = models.ForeignKey(Share)
    date = models.DateField(null=False)
    open = models.FloatField()
    close = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    volume = models.FloatField()


class ShareGroup(models.Model):
    name = models.CharField(max_length=32)
    shares = models.ManyToManyField(Share, blank=True)

    def __str__(self):
        return self.name
