from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    directed_by = models.CharField(max_length=50, null=True, blank=True, verbose_name='Directed by')
    genre = models.CharField(max_length=90, null=True, blank=True, verbose_name='Genre')
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


class Comments(models.Model):
    movie = models.OneToOneField('Movie', on_delete=models.CASCADE, null=True)
    text = models.TextField(null=True, blank=True, verbose_name='text')
    date_stamp = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name_plural = 'comments'
        verbose_name = 'comment'


class Cast(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, null=True)
    role = models.TextField(null=True, blank=True, verbose_name='Role')
    name = models.TextField(null=True, blank=True, verbose_name='Name')

    class Meta:
        verbose_name_plural = 'actors'
        verbose_name = 'actor'


class Staff(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, null=True)
    name = models.TextField(null=True, blank=True, verbose_name='Name')
    position = models.TextField(null=True, blank=True, verbose_name='Position')

    class Meta:
        verbose_name_plural = 'Film crew members'
        verbose_name = 'Film crew member'
