from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import *
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
    
  
    if request.method == 'POST': 
        form = PostForm(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
  
    else: 
        form = PostForm() 
    return render(request, 'home.html', {'form' : form}) 
  

    # return render(request, 'home.html')


def about(request):
    return render(request, 'about.html', {'title': 'About'})


class PostListView(ListView):
    model = Post
    template_name = 'home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']


class PostDetailView(DetailView):
    model = Post
