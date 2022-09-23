from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ViewSetMixin

from users.permissions import IsAuthorUser, is_owner_of_page, is_user_moderator

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
        if self.action in ['update', 'destory',
                           'retrieve']:
            permission_classes = [IsAdminUser | is_owner_of_page | is_user_moderator]
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

    def get_serializer_class(self):
        if self.action in ['update', 'destory',
                           'retrieve']:
            permission_classes = [IsAdminUser | IsAuthorUser | is_user_moderator]
        return [permission() for permission in permission_classes]
