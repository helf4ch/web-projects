from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User


class RegisterUser(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:login')
    

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    
    def get_success_url(self):
        return reverse_lazy('forum:index')
    

class UserProfile(generic.DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'userprofile'


class LogoutUser(LogoutView):
    template_name = 'users/logout.html'
    next_page = reverse_lazy('forum:index')
    