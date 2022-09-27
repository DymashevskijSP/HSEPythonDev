from django.db import models
from django.contrib.postgres.fields import ArrayField


class User(models.Model):
    name = models.CharField(max_length=30)
    login = models.CharField(max_length=40, primary_key=True)


class Meeting(models.Model):
    meeting_id = models.BigIntegerField(primary_key=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    name = models.CharField(max_length=120)
    users = ArrayField(
        models.CharField(max_length=40),
        verbose_name='login'
    )
