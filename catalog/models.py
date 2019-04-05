from django.db import models

# Create your models here.
class Bd(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)