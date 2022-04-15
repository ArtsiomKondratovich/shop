from django.urls import path, include

from .context_processor import current_city
from .views import main_page, new_user, Login, Logout, profile

app_name = 'main'
urlpatterns = [
    path('', main_page.as_view(), name='hello'),
    path('registration/', new_user, name='reg'),
    path('logout/', Logout.as_view(), name='logout'),
    path('login/', Login.as_view(), name='login'),
    path('profile/<int:pk>', profile, name='profile'),
    path('cont/', current_city, name='current'),
]
