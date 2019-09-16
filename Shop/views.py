from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from Shop.models import Game


def index(request):  # Checking homepage
    games = Game.objects.all().filter(is_published=True)
    context = {
        'games' : games,
        'nav' : 'index'
    }
    return render(request, 'Shop/index.html', context)


def game_page(request, game_id): # Products page
    game_page = get_object_or_404(Game, pk=game_id)
    context = {
        'game_page' : game_page
    }
    return render(request, 'Shop/game_page.html', context)

