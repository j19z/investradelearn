from django.contrib import admin

from .models import Post, Category, Comment


class CommentItemInLine(admin.TabularInline):  # This is to show the comments inside the post seccion
    model = Comment
    raw_id_fields = ['post']


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'category', 'status', 'created_at']
    list_filter = ['category', 'created_at', 'status']
    inlines = [CommentItemInLine]  # this is to add the comments in the post section.
    prepopulated_fields = {'slug': ('title',)}  # this is to automatically populate the slug field on the Admin

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}  # this is to automatically populate the slug field on the Admin


class CommentAdmin(admin.ModelAdmin):
    search_fields = ['title', 'body']
    list_display = ['name', 'post', 'created_at']



admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
