from django.urls import path
from apps.blog.views import get_blog, edit_blog, create_blog, delete_blog

urlpatterns = [
        path('list/', get_blog, name='blog_list'),
        path('edit/', edit_blog, name='edit_blog'),
        path('create/', create_blog, name='create_blog'),
        path('delete/<int:blog_id>', delete_blog, name='delete_blog')
    ]
