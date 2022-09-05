from django.contrib import admin
from .models import Post, Page, Tag

admin.register(Page, Post, Tag)
# Register your models here.
