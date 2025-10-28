from django.shortcuts import render, get_object_or_404
from .models import Blog, Category


# Create your views here.
def post_by_category(request, category_id):
    posts=Blog.objects.filter(category__id=category_id, status="Published").order_by('-created_at')
    category_title=Category.objects.get(id=category_id).category_name
    context={
        'posts':posts,
        'category_title':category_title,
    }
    return render(request, 'posts_by_category.html', context)
