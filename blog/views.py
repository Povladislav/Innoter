from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ViewSetMixin

from users.permissions import IsAuthorUser, IsUserModerator

from .models import Page, Post, Tag
from .serializers import PageSerializer, PostSerializer, TagSerializer


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

    def get_serializer_class(self):
        if self.action == "update" or self.action == "destroy" or self.action == "retrieve":
            permission_classes = [IsAdminUser, IsAuthorUser]
        return [permission() for permission in permission_classes]


class PageView(ViewSetMixin,
               GenericAPIView,
               ListModelMixin,
               CreateModelMixin,
               UpdateModelMixin,
               RetrieveModelMixin,
               DestroyModelMixin):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
