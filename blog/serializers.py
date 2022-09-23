from rest_framework import serializers

from users.models import User

from .models import Page, Post, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='page.owner')

    class Meta:
        model = Post
        fields = ['content', 'created_at','owner']


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"
