from django.contrib import admin
from django.urls import path

from .views import view_email, view_success

urlpatterns = [
    path('email/', view_email, name='email'),
    path('success/', view_success, name='success'),
]