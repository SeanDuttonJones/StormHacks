from django.urls import path
from .import views as blog_views
from .views import (
    PostListView,
    PostDetailView
)
# followed tutorial: https://www.youtube.com/watch?v=qDwdMDQ8oX4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=3
# for Blog creation html, views and other set up for the Blog
# used to learn jango and how to use html with it
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib import admin 

urlpatterns = [

    path('', PostListView.as_view(), name='Blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('',blog_views.home, name='Blog-home'),
    # path('image_upload', blog_views.home, name = 'image_upload'),
    # get post by primary key

    # path('about/', blog_views.about, name='Blog-about'),

    # path('post/new/', PostCreateView.as_view(), name='post-create'),

]





