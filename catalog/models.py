from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    content = models.TextField(null=True, blank=True, verbose_name='Content')
    year = models.CharField(max_length=4, verbose_name='Year')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Films'
        verbose_name = 'Film'


class MovieDescription(models.Model):
    movie = models.OneToOneField('Movie', on_delete=models.CASCADE, null=True)
    synopsis = models.TextField(null=True, blank=True, verbose_name='Synopsis')
    rate = models.FloatField(null=True, blank=True, verbose_name='Rate')

    class Meta:
        verbose_name_plural = 'descriptions'
        verbose_name = 'description'


class Comments:
    movie = models.OneToOneField('Movie', on_delete=models.CASCADE, null=True)
    text = models.TextField(null=True, blank=True, verbose_name='text')
    date_stamp = models.DateTimeField(auto_now_add=True, db_index=True)

