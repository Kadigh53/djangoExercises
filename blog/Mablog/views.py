from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post

# Create your views here.
class BlogView(ListView):
    model=Post
    context_object_name='blog_posts'
    template_name='home.html'

class BlogDetailView(DetailView):
    model=Post
    context_object_name='blogDposts'
    template_name='post_detail.html'

class BlogCreateView(CreateView):
    model=Post
    template_name='post_new.html'
    fields=['title','author','body']
    # success_url=Post.get_absolute_url()
