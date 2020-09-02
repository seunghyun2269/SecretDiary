from django.shortcuts import render
from .models import Post
from .forms import PostForm

def main(request):
    posts = Post.objects
    return render(request, 'create.html', {'posts':posts})

def diary(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'diary.html' {'post':post})

def create(request):
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('main')
    else: 
        form = PostForm()
    return render(request, 'create.html', {'form':form})

def board(request):
    return render(request, 'board.html')

def delete(request, pk):
    post = Post.objects.get(pk = pk)
    post.delete()
    return redirect('home')