from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    User = models.CharField(max_length=100)
    Email = models.EmailField()
    Message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    approve = models.BooleanField(default=False)

    def approved(self):
        self.approve = True
        self.save()

    def __str__(self):
        return self.User
