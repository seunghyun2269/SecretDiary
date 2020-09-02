from django import forms
from .models import Post

class PostForm(froms.ModelsForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'content']