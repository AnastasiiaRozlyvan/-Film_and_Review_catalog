from django.contrib import admin
from .models import Movie
from .models import MovieDescription


class BdAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'year')
    list_display_links = ('title', 'content', 'year')
    search_fields = ('title', 'content', 'year')


class MovieDescriptionAdmin(admin.ModelAdmin):
    list_display = ('synopsis', 'rate')
    list_display_links = ('synopsis', 'rate')
    search_fields = ('synopsis', 'rate')


admin.site.register(Movie, BdAdmin)
admin.site.register(MovieDescription, MovieDescriptionAdmin)
