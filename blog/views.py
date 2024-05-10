from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

class PostList(ListView):
    """Displays a list of all published posts."""
    model = Post
    queryset = Post.objects.filter(status=1)
    template_name = 'blog/blog.html'
    paginate_by = 6

class PostDetail(DetailView):
    """Displays a detailed view of a specific post."""
    model = Post
    template_name = 'blog/post_detail.html'

@method_decorator(login_required, name='dispatch')
class PostCreate(CreateView):
    """Provides a form to create a new post. Only accessible to logged-in users."""
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        form.instance.author = self.request.user
        if not self.request.user.is_superuser:
            form.instance.status = 0  # Set status to Draft if not superuser
        response = super().form_valid(form)
        if self.request.user.is_superuser and form.instance.status == 1:
            messages.success(self.request, "You have successfully published the blog post.")
        elif self.request.user.is_superuser and form.instance.status == 0:
            messages.success(self.request, "Your blog post is set to draft.")
        else:
            messages.success(self.request, "Your have successfully created your blog post. Your request is waiting for approval.")
        return response

@method_decorator(login_required, name='dispatch')
class PostUpdate(UpdateView):
    """Provides a form to update an existing post. Only accessible to logged-in users."""
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.user.is_superuser and form.instance.status == 1:
            messages.success(self.request, "You have successfully updated the blog post to published.")
        elif self.request.user.is_superuser and form.instance.status == 0:
            messages.success(self.request, "Your blog post update is set to draft.")
        else:
            messages.success(self.request, "You have successfully updated your blog post.")
        return response

@method_decorator(login_required, name='dispatch')
class PostDelete(DeleteView):
    """Allows a user to delete a post. Only accessible to logged-in users."""
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(request, "You have successfully deleted your blog post.")
        return response
