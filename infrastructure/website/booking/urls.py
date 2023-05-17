from django.urls import path
from .views import create_new, home

urlpatterns = [
    path('create-new', create_new),
    path('', home, name='home'),
]