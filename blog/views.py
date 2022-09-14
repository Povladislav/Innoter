from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.viewsets import ViewSetMixin
from rest_framework.permissions import AllowAny

from .models import Page, Post, Tag
from .serializers import PageSerializer, PostSerializer, TagSerializer

from users.permissions import IsUserModerator, IsAuthorUser


class TagView(ViewSetMixin,
              GenericAPIView,
              ListModelMixin,
              CreateModelMixin,
              UpdateModelMixin,
              RetrieveModelMixin,
              DestroyModelMixin):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostView(ViewSetMixin,
               GenericAPIView,
               ListModelMixin,
               CreateModelMixin,
               UpdateModelMixin,
               RetrieveModelMixin,
               DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PageView(ViewSetMixin,
               GenericAPIView,
               ListModelMixin,
               CreateModelMixin,
               UpdateModelMixin,
               RetrieveModelMixin,
               DestroyModelMixin):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
