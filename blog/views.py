from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

class PostList(ListView):
    """ Displays a list of all published posts """
    model = Post 
    queryset = Post.objects.filter(status=1)
    template_name = 'blog/blog.html'
    paginate_by = 8

class PostDetail(DetailView):
    """ Displays a detailed view of a specific post. """
    model = Post
    template_name = 'blog/post_detail.html'

@method_decorator(login_required, name='dispatch')
class PostCreate(CreateView):
    """ Provides a view to create a new post. Requires user to be logged in """
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

@method_decorator(login_required, name='dispatch')
class PostUpdate(UpdateView):
    """ Provides a view to update an existing post. Requires user to be logged in. """
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

@method_decorator(login_required, name='dispatch')
class PostDelete(DeleteView):
    """ Provides a view to delete a post. Requires user to be logged in. """
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog')  # Redirects to the blog list page after deletion.

def approve_post(request, pk):
    """ Allows superusers to approve posts by changing their status. """
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_superuser:
        post.status = 1
        post.save()
        return redirect('blog')
    else:
        return redirect('blog')