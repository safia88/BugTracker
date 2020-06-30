from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Customeuser(AbstractUser):
    profile = models.CharField(null=True, max_length=100)
    Age = models.IntegerField(null=True)


User = settings.AUTH_USER_MODEL


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    Description = models.TextField()
    filed_by = models.ForeignKey(
        User, related_name='filed_by', on_delete=models.CASCADE, null=False)
    assigned_to = models.ForeignKey(
        User, related_name='assigned_to', on_delete=models.CASCADE, null=True)
    completed_by = models.ForeignKey(
        User, related_name='completed_by', on_delete=models.CASCADE, null=True)
    LEVEL_CHOICES = (
        ('FIRST', 'New'),
        ('SECOND', 'In Progress'),
        ('THIRD', 'Done'),
        ('FOURTH', 'Invalid'),
    )
    status = models.CharField(
        max_length=40, choices=LEVEL_CHOICES, default='FIRST')
    time_submited = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
