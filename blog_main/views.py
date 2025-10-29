from django.shortcuts import render, redirect
from blogs.models import Category,Blog
from .form import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth 

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



def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:       # You can add a success message or redirect to login page here
        form = RegisterForm()
    context = {
        "form": form,
    }
    return render(request, "registration.html", context)


def login(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')

            user=auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                return redirect('home')
    form=AuthenticationForm()
    context={
        "form":form,
    }
    return render(request, "login.html", context)

def logout(request):
    auth.logout(request)
    return redirect('home')