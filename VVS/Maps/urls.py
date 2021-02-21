from django.urls import path
from . import views as map_views

urlpatterns = [
    path("", map_views.maps_page)
]