from app.admin import ModelAdmin, admin
from pages.models import Page


@admin.register(Page)
class PageAdmin(ModelAdmin):
    fields = [
        'title',
        'slug',
        'content',
        'created_at',
        'updated_at',
    ]
    list_display = [
        'title',
        'slug',
        'content',
    ]
