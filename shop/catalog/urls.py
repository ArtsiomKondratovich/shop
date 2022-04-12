from django.urls import path, include

from .views import main_page, new_user, Login, Logout
app_name = 'main'
urlpatterns = [
    path('', main_page.as_view(), name='hello'),
]