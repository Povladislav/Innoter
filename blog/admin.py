from django.contrib import admin
from .models import Post, Page, Tag

admin.site.register(Page)
admin.site.register(Post)
admin.site.register(Tag)
