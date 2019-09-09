from django.contrib import admin
from Shop.models import Game

# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'id')
    list_display_links = ('title',)

admin.site.register(Game, GameAdmin)