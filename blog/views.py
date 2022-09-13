from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin, UpdateModelMixin)
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSetMixin

from .models import Tag, Post
from .serializers import TagSerializer, PostSerializer


class TagView(ViewSetMixin,
              GenericAPIView,
              ListModelMixin,
              CreateModelMixin,
              UpdateModelMixin,
              DestroyModelMixin):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]


class PostView(ViewSetMixin,
               GenericAPIView,
               ListModelMixin,
               CreateModelMixin,
               UpdateModelMixin,
               DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
