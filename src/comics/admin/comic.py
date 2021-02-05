from django.contrib import admin

from comics.models import Comic
from default.admin import DefaultAdmin


@admin.register(Comic)
class ComicAdmin(DefaultAdmin):
    fields = ['slug', 'owner']
    list_display = [
        '__str__',
        'owner',
    ]
