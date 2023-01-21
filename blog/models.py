from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    title = models.CharField(max_length=200, help_text='200 symbols max', db_index=True)
    content = models.TextField(max_length=5000, blank=True, null=True, help_text='5000 symbols max')
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.title
