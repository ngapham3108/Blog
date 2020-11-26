from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=20, default='Blog Site')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cats = models.CharField(max_length=50, default='Others')
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title) + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.pk)])


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

