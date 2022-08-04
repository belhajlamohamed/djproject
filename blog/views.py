from multiprocessing import context
from django.shortcuts import render
from .models import Post
from django.views.generic.list import ListView


class PostListView(ListView):
    model = Post 
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    
