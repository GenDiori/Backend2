from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Post
from .forms import ThreadForm, PostForm

# Главная страница - перенаправление на список тредов
def home(request):
    return redirect('thread-list')

# Список всех Thread + форма создания Thread в модальном окне
def thread_list(request):
    threads = Thread.objects.all()
    form = ThreadForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('thread-list')

    return render(request, 'post/thread_list.html', {'threads': threads, 'form': form})

# Детальная страница Thread + список Post + форма создания Post
def thread_detail(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    posts = thread.posts.all()
    form = PostForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        post.thread = thread
        post.save()
        return redirect('thread-detail', pk=pk)

    return render(request, 'post/thread_detail.html', {'thread': thread, 'posts': posts, 'form': form})

# Удаление Thread
def thread_delete(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    thread.delete()
    return redirect('thread-list')

# Редактирование Thread
def thread_edit(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    form = ThreadForm(request.POST or None, instance=thread)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('thread-detail', pk=pk)

    return render(request, 'post/thread_edit.html', {'form': form, 'thread': thread})

# Удаление Post
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    thread_id = post.thread.id
    post.delete()
    return redirect('thread-detail', pk=thread_id)

# Редактирование Post
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('thread-detail', pk=post.thread.id)

    return render(request, 'post/post_edit.html', {'form': form, 'post': post})
