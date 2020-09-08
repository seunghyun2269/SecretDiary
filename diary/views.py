from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Post
from .forms import PostForm


def board(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'board.html', context)

def diarypage(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "diarypage.html", {'post': post})

def main(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'main.html', context)

'''
def diary(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'diary.html', {'post':post})
'''

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else: 
        form = PostForm()
    return render(request, 'create.html', {'form':form})

'''
def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('diarypage', post_id)
        
    else:
        form = PostForm(instance = post)
    return render(request, 'update.html', {'form': form})
'''

def delete(request, post_id):
    post = Post.objects.get(pk = post_id)
    post.delete()
    return redirect('main')
