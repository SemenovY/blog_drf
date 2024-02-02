from django.contrib import admin

from .models import Blog, BlogPost


@admin.register(Blog)
class BlogAdmin(admin.Admin):
    pass


@admin.register(BlogPost)
class BlogPostAdmin(admin.Admin):
    pass
