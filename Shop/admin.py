from django.contrib import admin

# Register your models here.
from Shop.models import Game


class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'id', 'is_published')
    list_display_links = ('title',)
    list_editable = ('is_published',)


admin.site.register(Game, GameAdmin)
