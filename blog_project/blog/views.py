from _ast import Delete

from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView, DetailView,
                                  ListView, DeleteView, CreateView, UpdateView)
# for API
import requests


# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):  # return data from post model.
    context_object_name = 'all_post'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):  # return details about the post specified by PK.
    model = Post
    # context_object_name = 'post_detail'


class CreatePostView(LoginRequiredMixin, CreateView):
    # create post view needs access "login required" and after login
    # we need to set url that we want to go to it after login.
    # the form we need to use it
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm
    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    template_name = 'post_draft_list.html'

    context_object_name = 'all_draft_post'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')


################################################
#                comment template              #
################################################
@login_required()
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required()
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  # because in the comment >> post << is FK to the post model
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})


@login_required()
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)  # comment.post >> post.pk


@login_required()
def comment_remove(requset, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk  # we save it in extra variable because when we delete, it's cannot remember the post PK
    comment.delete()
    return redirect('post_detail', pk=post_pk)


################################################
#                test design template          #
################################################
class Test(TemplateView):
    template_name = 'test.html'


################################################
#                API test template             #
################################################
def myapi(request):
    response = requests.get('http://34.244.171.232/api/v1/product/?search=iphone&action_type=DB')
    results = response.json()
    return render(request, 'blog/myapi.html', {'results': results})
