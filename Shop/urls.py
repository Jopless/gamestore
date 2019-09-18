from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:game_id>', views.game_page, name='game_page'),
]