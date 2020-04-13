from django.db import models
from ckeditor import fields as ckeditor
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Post(models.Model):
    """ The Post models for blog posts, One To Many relationship """
    # if user got deleted, delete all related posts to user
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = ckeditor.RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
