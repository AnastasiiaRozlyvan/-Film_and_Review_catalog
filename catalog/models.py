from django.db import models


class Bd(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    content = models.TextField(null=True, blank=True, verbose_name='Content')

    class Meta:
        verbose_name_plural = 'Films'
        verbose_name = 'Film'
