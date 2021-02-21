from django.urls import path
from . import views as blog_views
from .views import PostListView, PostDetailView, PostCreateView
# followed tutorial: https://www.youtube.com/watch?v=qDwdMDQ8oX4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=3
# for blog creation html, views and other set up for the blog
# used to learn jango and how to use html with it
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',blog_views.home, name='blog-home'),
    # get post by primary key
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # path('about/', blog_views.about, name='blog-about'),

    # path('post/new/', PostCreateView.as_view(), name='post-create'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
