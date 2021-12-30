from django.db import models
from django.contrib.auth.models import User
from django.db. models.signals import pre_save,post_save
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver
from django.urls import reverse
from datetime import datetime
from django.core.validators import MinLengthValidator








class Category(models.Model):
    title = models.CharField(max_length=30, default="Random")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

class Tag(models.Model):
    title = models.CharField(max_length=30, default="Random")

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=200,validators=[MinLengthValidator(15)], default="Title")
    slug = models.SlugField(unique=True)

    content = models.TextField()
    timestamp = models.DateField(default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)



    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'comment {} by {}'.format(self.body, self.user)

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)













