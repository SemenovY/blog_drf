from django.contrib import admin

from users.models import Blog, BlogPost


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog', 'created_at',)
    search_fields = ('title', 'blog__user__username',)
