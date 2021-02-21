from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# test data
posts = [
    {
        'author': 'Nate the Great',
        'title': 'Why we need Fair trade',
        'content': 'First post content',
        'date_posted': 'January 1, 2021'
    },
    {
        'author': 'Jas',
        'title': 'Why are you helping the farmers?',
        'content': 'Second post content',
        'date_posted': 'January 20, 2021'
    }
]


# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'About'})


class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = [-'date_poster']
