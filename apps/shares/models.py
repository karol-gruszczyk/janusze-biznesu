from django.db import models


class ShareManager(models.Manager):

    @classmethod
    def get_records(cls, share):
        if type(share) != Share:
            raise TypeError("type 'Share' expected")
        return ShareRecord.objects.filter(share__pk=share.pk)

    @classmethod
    def get_groups(cls, share):
        if type(share) != Share:
            raise TypeError("type 'Share' expected")
        return share.sharegroup_set.all()


class Share(models.Model):
    name = models.CharField(max_length=32, db_index=True, unique=True)
    verbose_name = models.CharField(max_length=64, null=True, blank=True)
    updated_daily = models.BooleanField(default=False)
    last_updated = models.DateTimeField(null=True)
    first_record = models.DateField(null=True)
    last_record = models.DateField(null=True)
    num_records = models.PositiveIntegerField(null=True)

    objects = ShareManager()

    class Meta:
        get_latest_by = 'last_updated'

    def __str__(self):
        return self.verbose_name if self.verbose_name else self.name


class ShareSet(models.Model):
    shares = models.ManyToManyField(Share)


class ShareRecord(models.Model):
    share = models.ForeignKey(Share, null=False, db_index=True, related_name='records')
    date = models.DateField(null=False, db_index=True)
    open = models.FloatField(null=False)
    close = models.FloatField(null=False)
    high = models.FloatField(null=False)
    low = models.FloatField(null=False)
    volume = models.FloatField(null=False)

    class Meta:
        unique_together = ('share', 'date',)
        index_together = ['share', 'date']


class ShareGroup(models.Model):
    name = models.CharField(max_length=32, db_index=True, unique=True)
    verbose_name = models.CharField(max_length=64, null=True)
    shares = models.ManyToManyField(Share, blank=True)

    def __str__(self):
        return self.verbose_name if self.verbose_name else self.name
