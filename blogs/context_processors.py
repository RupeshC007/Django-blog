from blogs.models import Category

def get_categories(request):
    category = Category.objects.all()
    return {'category': category}