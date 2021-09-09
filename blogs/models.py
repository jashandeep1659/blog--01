from django.db import models
from taggit.managers import TaggableManager
# from tinymce.models import HTMLField
from tinymce import models as tinymce_models

# Create your models here.
class Category(models.Model):
    name  = models.CharField(max_length=100)
    slug = models.SlugField()
    image  = models.ImageField(upload_to="category/",)

    def __str__(self):
        return self.name

class Blog(models.Model):
    id  = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=100)
    tags = TaggableManager()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField()
    image  = models.ImageField(upload_to="blogs/",)
    overview  = models.CharField(max_length=100)
    detail = tinymce_models.HTMLField()
    writer = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default=True)
    views   = models.BigIntegerField(default=0)
    def __str__(self):
        return self.name

class Quote(models.Model):
    quote = models.TextField()
    by = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.by

class Ad(models.Model):
    ad_banner = models.ImageField(upload_to="ad/")
    link = models.CharField( max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link

class About_me(models.Model):
    image = models.ImageField(upload_to="user/")
    detail = models.TextField()
    instagram  = models.CharField(max_length=300)
    twiter  = models.CharField(max_length=300)
    linked_in  = models.CharField(max_length=300)
    youtube  = models.CharField(max_length=300)
    facebook  = models.CharField(max_length=300)
    email  = models.CharField(max_length=300)

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    full_name = models.CharField( max_length=100)
    email  = models.EmailField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name
