from django.contrib import admin

# Register your models here.
from Shop.models import Game


class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'id')
    list_display_links = ('title',)


admin.site.register(Game, GameAdmin)
