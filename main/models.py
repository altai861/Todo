from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.timezone import now

# Create your models here.
class problem(models.Model):
    whose_problem = models.CharField(max_length=250, null=True)
    title = models.CharField(max_length=250)
    description = models.TextField(null=True)
    deadline = models.DateTimeField(default=now)


