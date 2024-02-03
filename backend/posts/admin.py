from django.contrib import admin

from users.models import Blog, BlogPost


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'blog', 'title', 'created_at',)
    search_fields = ('title', 'blog__user__username',)
