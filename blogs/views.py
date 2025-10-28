from django.shortcuts import render
from .models import Blog, Category
from django.http import HttpResponse
from django.db.models import Q


# Create your views here.
def post_by_category(request, category_id):
    posts=Blog.objects.filter(category__id=category_id, status="Published").order_by('-created_at')
    category_title=Category.objects.get(id=category_id).category_name
    context={
        'posts':posts,
        'category_title':category_title,
    }
    return render(request, 'posts_by_category.html', context)


def blog_detail(request, slug):
    single_post = Blog.objects.get(slug=slug, status="Published")
    context = {
        'single_post': single_post,
    }
    return render(request, 'blog_detail.html', context)

def socialmedia_detail(request, socialmedia_id):
    return HttpResponse(f"Social Media Detail Page for ID: {socialmedia_id}")

def blog_search(request):
    keyword = request.GET.get('keyword')
    blogs= Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status="Published") 
    context={
        'blogs': blogs,
        'keyword': keyword,
    }
    
    return render(request, 'blog_search.html', context)