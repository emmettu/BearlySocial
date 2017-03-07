from django.contrib import admin
from post.models import *

# Register admin models for admin interface
class PostAdmin(admin.ModelAdmin):
    fields = ('id', 'post', 'author', 'content', 'publishDate')

# Register your models here.
admin.site.register(Post, PostAdmin)
