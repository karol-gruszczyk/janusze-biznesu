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
    visible_name = models.CharField(max_length=64, null=True, blank=True)
    updated_daily = models.BooleanField(default=False)
    first_record = models.DateField(null=True)
    last_record = models.DateField(null=True)
    records = models.PositiveIntegerField(null=True)

    objects = ShareManager()

    def __str__(self):
        return self.visible_name if self.visible_name else self.name


class ShareRecord(models.Model):
    share = models.ForeignKey(Share, null=False, db_index=True)
    date = models.DateField(null=False, db_index=True)
    open = models.FloatField(null=False)
    close = models.FloatField(null=False)
    high = models.FloatField(null=False)
    low = models.FloatField(null=False)
    volume = models.FloatField(null=False)


class ShareGroup(models.Model):
    name = models.CharField(max_length=32, db_index=True, unique=True)
    visible_name = models.CharField(max_length=64, null=True)
    shares = models.ManyToManyField(Share, blank=True)

    def __str__(self):
        return self.visible_name if self.visible_name else self.name
