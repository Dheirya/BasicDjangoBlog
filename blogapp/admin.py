from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'posted_on', 'id')
    search_fields = ['title', 'content']


admin.site.register(Post, PostAdmin)
