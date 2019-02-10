from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post
from .forms import PostForm
from rest_framework import viewsets
from .serializers import PostSerializer

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            try:
                return redirect('post_detail', pk=post.pk)
            except ValueError:
                raise("There's has been an issue")
                
    else:
        return render(request, 'blog/post_new.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            try:
                return redirect('post_detail', pk=post.pk)
            except ValueError:
                raise("There's has been an issue")
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def unpublished_posts(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_unpublished_list', {})

class PostViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows Post to be viewed or edited """
    queryset = Post.objects.all().order_by('-created_date')
    serializer_class = PostSerializer

