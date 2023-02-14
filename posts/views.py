from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    template_name = "list.html"
    model = Post