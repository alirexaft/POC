from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    def __str__(self):
        return self.username


class MetaData(models.Model):
    request_date = models.DateTimeField(default=timezone.now)
    request_user = models.ForeignKey(User, on_delete=models.CASCADE)
    line_count = models.PositiveIntegerField(null=False)
    end_req_time = models.DateTimeField()
