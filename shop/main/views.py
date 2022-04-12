from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from .forms import NewUserForm


def main_page(request):
    return render(request, 'main_page.html')


def new_user(request):
    if request.method == 'POST':
        user = NewUserForm(request.POST)
        if user.is_valid():
            new_user = User.objects.create_user(**user.cleaned_data)
            return redirect('main:hello')
    else:
        form = NewUserForm()
        context = {'form': form}
        return render(request, 'registration.html', context)

class Login(LoginView):
    template_name = 'Login.html'
    def get_success_url(self):
        return reverse_lazy('main:hello')

class Logout(LogoutView):
    next_page = "main:hello"