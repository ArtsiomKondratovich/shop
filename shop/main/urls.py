from django.urls import path, include

from main.views import hello

app_name = 'main'
urlpatterns = [
    path('', hello, name='hello'),
]
