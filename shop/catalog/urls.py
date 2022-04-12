from django.urls import path, include

from catalog.views import subcat_detail

app_name = 'catalog'
urlpatterns = [
    path('/<int:pk>/', subcat_detail , name='cat'),

]