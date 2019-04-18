from django.contrib import admin
from .models import Movie
from .models import MovieDescription
from .models import Cast, Staff


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'directed_by', 'year', 'genre')
    list_display_links = ('title', 'directed_by', 'year', 'genre')
    search_fields = ('title', 'directed_by', 'year', 'genre')


class MovieDescriptionAdmin(admin.ModelAdmin):
    list_display = ('synopsis', 'rate')
    list_display_links = ('synopsis', 'rate')
    search_fields = ('synopsis', 'rate')


class CastAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
    list_display_links = ('name', 'role')
    search_fields = ('name', 'role')


class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    list_display_links = ('name', 'position')
    search_fields = ('name', 'position')


admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieDescription, MovieDescriptionAdmin)
admin.site.register(Cast, CastAdmin)
admin.site.register(Staff, StaffAdmin)
