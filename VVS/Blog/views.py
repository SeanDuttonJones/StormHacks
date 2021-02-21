from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
# test data
from .models import Post


# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'About'})


class PostListView(ListView):
    model = Post
    template_name = 'home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'  # <app>/<model>_<viewtype>.html


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']