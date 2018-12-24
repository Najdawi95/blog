from _ast import Delete

from django.shortcuts import render
from blog.models import Post, Comment
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import PostForm, CommentForm
from django.views.generic import (View, TemplateView, DetailView,
                                  ListView, DeleteView, CreateView)


# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):  # return data from post model.
    model = Post
    context_object_name = 'all_post'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):  # return details about the post specified by PK.
    model = Post
    context_object_name = 'post_detail'


class CreatePostView(LoginRequiredMixin, CreateView):
    # create post view needs access "login required" and after login
    # we need to set url that we want to go to it after login.
    # the form we need to use it
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm
    model = Post
