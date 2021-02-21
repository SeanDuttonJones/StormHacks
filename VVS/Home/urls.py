from django.urls import path
from . import views as home_views

urlpatterns = [
    path('', home_views.home, name='homepage'),
    path('about/', home_views.about, name='aboutpage'),
]