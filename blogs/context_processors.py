from blogs.models import Category, SocialMedia


def get_categories(request):
    category = Category.objects.all()
    return {'category': category}

def get_socialmedia(request):
    socialmedia = SocialMedia.objects.all()
    return {'socialmedia': socialmedia}