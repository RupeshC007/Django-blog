from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    #category urls
    path("categories/",views.categories, name="categories"),
    path("categories/add/",views.add_category, name="add_category"),
    path("categories/edit/<int:id>/",views.edit_category, name="edit_category"),
    path("categories/delete/<int:id>/",views.delete_category, name="delete_category"),

    #blog urls
    path("blogs/",views.blogs, name="blogs"),
    path("blogs/add/",views.add_blog, name="add_blog"),
    path("blogs/edit/<int:id>",views.edit_blog, name="edit_blog"),
    path("blogs/delete/<int:id>",views.delete_blog, name="delete_blog"),
]