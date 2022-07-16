from django.views.generic import ListView
from .models import Post


class BlogView(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'
    ordering = ['-posted_on']

