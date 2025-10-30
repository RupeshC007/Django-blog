from django.shortcuts import render, redirect
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .form import CategoryForm, BlogForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count= Category.objects.all().count()
    blog_count= Blog.objects.all().count()
    context={
        'category_count':category_count,
        'blog_count':blog_count,
    }
    return render(request, "dashboard/dashboard.html", context )

def categories(request):
    return render(request, "dashboard/categories.html" )
                  
def add_category(request):
    if request.method=="POST":
        form= CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form= CategoryForm()
    context={
        'form':form,
    }
    return render(request, "dashboard/add_category.html", context )


def edit_category(request, id):
    category_title= Category.objects.get(id=id)
    if request.method=="POST":
        form= CategoryForm(request.POST, instance=category_title)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form= CategoryForm(instance=category_title)
    context={
        'form':form,
        'category_title':category_title,
    }
    
    return render(request, "dashboard/edit_category.html", context )

def delete_category(request, id):
    category_title= Category.objects.get(id=id)
    category_title.delete()
    return redirect('categories')



def blogs(request):
    posts= Blog.objects.all()
    context={
        'posts':posts,
    }
    return render(request, "dashboard/blogs.html", context )


def add_blog(request):
    if request.method=="POST":
        form= BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            title=form.cleaned_data("title")
            title.slug=slugify(title) +"-"+str(post.id) 
            return redirect('blogs')
    form= BlogForm()
    context={
        'form':form,
    }
    return render(request, "dashboard/add_blog.html", context )


def edit_blog(request, id):
    post=Blog.objects.get(id=id)
    if request.method=="POST":
        form= BlogForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blogs')
    form=BlogForm(instance=post)
    context={
        'form': form,
        'post':post
    }
    return render(request, "dashboard/edit_blog.html", context)


def delete_blog(reuest, id):
    post=Blog.objects.get(id=id)
    post.delete()
    return redirect("blogs")



def users(request):
    users=User.objects.all()
    context={'users':users}

    return render(request, "dashboard/users.html", context)
