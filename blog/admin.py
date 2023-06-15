from django.contrib import admin

from .models import Page, Post, Tag

admin.site.register(Page)
admin.site.register(Post)
admin.site.register(Tag)
