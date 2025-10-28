from django.contrib import admin
from .models import Category, Blog, SocialMedia

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'status', 'is_featured', 'category')
    search_fields=('id','title', 'author__username', 'category__categoty_name','status')
    list_editable = ('status', 'is_featured')
# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)   
admin.site.register(SocialMedia)