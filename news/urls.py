from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.news_index, name='news'),
    path('<int:news_id>', views.news_page, name='news_page')
]