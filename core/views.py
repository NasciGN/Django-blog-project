from django.shortcuts import render
from django.views.generic import ListView, DetailView
from core.models import Post


# Create your views here.

class ListarPostsListView(ListView):
    context_object_name = 'posts'
    template_name = 'index.html'
    queryset = Post.publicados.filter(status='publicado')
    paginate_by = 2

class ExtendPost(DetailView):
    context_object_name = 'post'
    template_name = 'includes/post.html'
    model = Post


