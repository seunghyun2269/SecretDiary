from django.db import models
from django.utils import timezone

class Post(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL) # User모델의 userid 참조
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title