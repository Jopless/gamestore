from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.

# CUSTOM LOGIN REGISTRATION

# def register(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         username = request.POST['username']
#         password = request.POST['password']
#         password2 = request.POST['password2']
#         # Check if passwords match
#         if password == password2:
#             # Check username
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, 'That username is taken')
#                 return redirect('register')
#             else:
#                 # Check email
#                 if User.objects.filter(email=email).exists():
#                     messages.error(request, 'That email is being used')
#                     return redirect('register')
#                 else:
#                     # looks good
#                     user = User.objects.create_user(username=username, password=password, email=email)
#                     # Login after register
#                     user.save()
#                     messages.success(request, 'You are now registered and can log in')
#                     return redirect('login')
#         else:
#             messages.error(request, 'Passwords do not match')
#             return redirect('register')
#     else:
#         return render(request, 'accounts/../templates/registration/register.html')


# def login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = auth.authenticate(username=username, password=password)
#         # if user is found in database
#         if user is not None:
#             auth.login(request, user)
#             messages.success(request, 'You are now logged in')
#             return redirect('/')
#         else:
#             messages.error(request, 'Invalid credentials')
#             return redirect('login')
#     return render(request, 'accounts/../templates/registration/login.html')


# def logout(request):
#     if request.method == "POST":
#         auth.logout(request)
#         messages.success(request, 'You are now logged out')
#     return redirect(request, 'index')

class Register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/register.html'
