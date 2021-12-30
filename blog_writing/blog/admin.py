from django.contrib import admin
from .models import Category, Blog, Comment, Tag
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'timestamp', 'author')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'timestamp', 'author', 'categories', 'tags')
    list_per_page = 20

    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
