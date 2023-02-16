from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post


class PostListView(ListView):
    template_name = "list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "detail.html"
    model = Post

class PostCreateView(CreateView):
    template_name = "new.html"
    model = Post
    fields = ["title", "subtitle", "body"]