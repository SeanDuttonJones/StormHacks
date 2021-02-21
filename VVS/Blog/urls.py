from django.urls import path
from . import views as blog_views
# followed tutorial: https://www.youtube.com/watch?v=qDwdMDQ8oX4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=3
# for blog creation html, views and other set up for the blog
# used to learn jango and how to use html with it

urlpatterns = [
    path('', blog_views.home, name='blog-home'),
    path('about/', blog_views.about, name='blog-about'),
]