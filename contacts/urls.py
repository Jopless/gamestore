from django.contrib import admin
from django.urls import path

from contacts import views
from .views import view_email, view_success

urlpatterns = [
    path('links/', views.socbutton, name='links'),
    path('email/', view_email, name='email'),
    path('success/', view_success, name='success'),
]