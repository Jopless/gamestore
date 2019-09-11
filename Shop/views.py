from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from Shop.models import Game

# Create your views here.

# Testing models
# def get_games(request):
#     if request.method == 'GET':
#         game = Game.objects.all()[0]
#         return HttpResponse(str(game.title) + " UAH" + str(game.price))


def index(request):  # Checking homepage
    games = Game.objects.all().filter(is_published=True)
    if request.method == 'GET':
        return render(request, 'index.html', {"games": games})


def game_page(request, game_id):
    game_page = get_object_or_404(Game, pk=game_id)
    context = {
        'game_page' : game_page
    }
    return render(request, 'game_page.html', context)

