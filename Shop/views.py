from django.shortcuts import render
from django.http import HttpResponse
from Shop.models import Game

# Create your views here.

# Testing models
# def get_games(request):
#     if request.method == 'GET':
#         game = Game.objects.all()[0]
#         return HttpResponse(str(game.title) + " UAH" + str(game.price))


def index(request):  # Checking homepage
    if request.method == 'GET':
        return render(request, 'index.html')
