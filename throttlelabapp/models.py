from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=15)
    real_name = models.CharField(max_length=30)
    tz=models.CharField(max_length=40)
    activity_periods=models.CharField(max_length=500)

    def __str__(self):
        return self.user_id
