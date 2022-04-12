from django.urls import path, include

from .views import main_page, new_user, Login, Logout
app_name = 'main'
urlpatterns = [
    path('', main_page, name='hello'),
    path('registration/', new_user, name='reg'),
    path('logout/', Logout.as_view( ), name='logout'),
    path('login/', Login.as_view(), name='login'),
]
