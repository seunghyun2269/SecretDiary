from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Post
from .forms import PostForm

<<<<<<< HEAD

# Create your views here.

def board(request):
    return render(request, "board.html")

def diarypage(request):
    return render(request, "diarypage.html")
=======
def main(request):
    posts = Post.objects
    return render(request, 'create.html', {'posts':posts})

def diary(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'diary.html', {'post':post})

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
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
>>>>>>> 58d59258a8195ed83c69d40164ce88191bfb71be
