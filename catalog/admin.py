from django.contrib import admin
from .models import Movie
from .models import MovieDescription
from .models import Comments


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'year')
    list_display_links = ('title', 'content', 'year')
    search_fields = ('title', 'content', 'year')


class MovieDescriptionAdmin(admin.ModelAdmin):
    list_display = ('synopsis', 'rate')
    list_display_links = ('synopsis', 'rate')
    search_fields = ('synopsis', 'rate')


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('text', 'date_stamp')
    list_display_links = ('text', 'date_stamp')
    search_fields = ('text', 'date_stamp')


admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieDescription, MovieDescriptionAdmin)
admin.site.register(Comments, CommentsAdmin)
