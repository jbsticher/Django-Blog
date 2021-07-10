from .models import Post
from django.views.generic import ListView, DetailView


class HomePageView(ListView):
    template_name = 'home.html'
    model = Post
    context_object_name = 'posts_list'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
