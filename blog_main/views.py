from django.shortcuts import render
from blogs.models import Category,Blog

def home(request):
    category=Category.objects.all()
    featured_posts=Blog.objects.filter(is_featured=True).order_by('-created_at')
    recent_posts=Blog.objects.filter(is_featured=True, status="Published").order_by('-created_at')
    context={
        "category":category,
        "featured_posts":featured_posts,
        "recent_posts":recent_posts,
    }
    return render(request, "home-blogs.html", context)
