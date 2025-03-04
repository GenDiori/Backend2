from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from .models import Post
from .forms import PostForm


def todo_list(request):
    posts = Post.objects.all()
    return render(request, 'post/todo_list.html', {'posts': posts})

def todo_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post/todo_detail.html', {'post': post})

def todo_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = PostForm()
    return render(request, 'post/todo_form.html', {'form': form})

def todo_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('todo_list')
