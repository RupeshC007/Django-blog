from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name
    
STATUS_CHOICES = (
    ("Draft", "Draft"),
    ("Published", "Published"),
)

class Blog(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200, unique=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image=models.ImageField(upload_to='uploads/%Y/%m/%d', null=True, blank=True)
    short_description=models.TextField()
    blog_body=models.TextField()
    status= models.CharField(max_length=50, choices=STATUS_CHOICES, default=0)
    is_featured=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)  
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title