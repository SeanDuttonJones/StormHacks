from django.urls import path
from . import views as home_views
from VVS.Maps import views as map_views

urlpatterns = [

    path('Maps/' , map_views.maps_page , name = 'index-home'),
    path('login/', home_views.login_page, name = 'login-home'),
    path('logout/', home_views.logout_page, name = 'logout-home'),
    path('register/', home_views.registration_page, name = 'registration-home'),
    path('business/', home_views.business_page, name = 'business-home'),
    path('shopper/', home_views.shopper_page, name = 'shopper-home'),

]