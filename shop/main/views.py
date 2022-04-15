from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.sessions.backends.db import SessionStore
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView

from .context_processor import current_city
from .forms import NewUserForm
from .models import Shop, City


class main_page(ListView):
    def pp(self):
        print(self.__dict__)

    template_name = 'main_page.html'
    model = Shop
    context_object_name = 'objects'


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


def profile(request, pk):
    return render(request, 'profile.html')