from django.urls import path, include

from accounts import views

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
]
