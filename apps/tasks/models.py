from django.db import models


class TaskStatus(models.Model):
    name = models.CharField(max_length=64)
    datetime_added = models.DateTimeField(auto_now_add=True)
    execution_date = models.TimeField(blank=True)
    progress = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
