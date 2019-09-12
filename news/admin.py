from django.contrib import admin

# Register your models here.

from news.models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'is_published')
    list_display_links = ('title',)
    list_editable = ('is_published',)

admin.site.register(News, NewsAdmin)