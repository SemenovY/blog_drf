from django.contrib import admin

from users.models import Blog, BlogPost


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass
