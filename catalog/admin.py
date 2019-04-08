from django.contrib import admin
from .models import Bd

class BdAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


admin.site.register(Bd, BdAdmin)
