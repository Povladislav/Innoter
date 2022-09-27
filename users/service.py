import datetime

from django.db.models import Q
from django.utils import timezone
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from blog.models import Page, Post
from blog.serializers import PostSerializer, PageSerializer, UserPageSerializer

from users.serializers import UserSerializer

from .models import User
from .permissions import IsOwnerOfPage, IsUserAdm, IsUserModerator


class BanUsersView(GenericAPIView):
    permission_classes = [IsUserAdm]

    def post(self, request, id):
        time = self.request.data.get("bantime")
        if time is None:
            user_to_ban = User.objects.get(pk=id)
            page_of_users_to_ban = Page.objects.filter(owner=user_to_ban)
            page_of_users_to_ban.delete()
            user_to_ban.is_active = False
            user_to_ban.is_blocked = True
            user_to_ban.save()
            return Response({"banned": "successfully permanently banned"})
        user_to_ban = User.objects.get(pk=id)
        page_of_users_to_ban = Page.objects.filter(owner=user_to_ban)
        for page in page_of_users_to_ban:
            page.time_before_unban = timezone.now() + datetime.timedelta(minutes=time)
            page.is_blocked = True
            page.save()
        user_to_ban.is_blocked = True
        user_to_ban.time_before_unban = timezone.now() + datetime.timedelta(minutes=time)
        user_to_ban.save()
        return Response({"banned": f"successfully banned for {time} minutes"})


class BanPagesView(GenericAPIView):
    permission_classes = [IsUserAdm | IsUserModerator]

    def post(self, request, id):
        time = self.request.data['bantime']
        page_to_ban = Page.objects.get(pk=id)
        page_to_ban.is_blocked = True
        page_to_ban.time_before_unban = timezone.now() + datetime.timedelta(minutes=time)
        page_to_ban.save()
        return Response({"banned": f"page successfully banned for {time} minutes"})


class FollowpageView(GenericAPIView):
    def get(self, request, id):
        page = Page.objects.get(pk=id)
        user = request.user
        if page.is_private:
            page.follow_requests.add(user)
        else:
            page.followers.add(user)
        return Response({"subscribed": f"user {user} successfully subscribed on {page}"})


class AcceptAllFollowersPageView(GenericAPIView):
    permission_classes = [IsOwnerOfPage]
    queryset = Page.objects.all()

    def put(self, request, pk):
        page = self.get_object()
        request.page = page
        if page.is_private:
            users = page.follow_requests.all()
            page.followers.add(*users)
            page.follow_requests.remove(*users)
            return Response({"accepted": "users were successfully accepted"})
        else:
            return Response({"accepted": "page is not private!"})


class AcceptFollowerForPageView(GenericAPIView):
    permission_classes = [IsOwnerOfPage]
    queryset = Page.objects.all()

    def put(self, request, pk, idOfUser):
        page = self.get_object()
        if page.is_private:
            user = page.follow_requests.get(pk=idOfUser)
            page.followers.add(user)
            return Response({"accepted": "user was successfully accepted"})
        else:
            return Response({"accepted": "page is not private!"})


class LikePostView(GenericAPIView):

    def post(self, request, id):
        post_to_like = Post.objects.get(id=id)
        request.user.likes.add(post_to_like)
        return Response({"liked": "successfully"})


class UnlikePostView(GenericAPIView):

    def post(self, request, id):
        post_to_like = Post.objects.get(id=id)
        request.user.likes.remove(post_to_like)
        return Response({"unliked": "successfully"})


class ShowNewsView(GenericAPIView):
    def get(self, request):
        posts = Post.objects.filter(Q(page__owner=request.user) | Q(page__followers=request.user))
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class ShowLikedPosts(GenericAPIView):
    def get(self, request):
        posts = Post.objects.filter(liked_posts=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class SearchPageView(GenericAPIView):
    def post(self, request):
        name = request.data.get("name")
        uuid = request.data.get("uuid")

        username = request.data.get("username")
        pages = Page.objects.filter(Q(name=name) | Q(uuid=uuid)).first()
        users = User.objects.filter(username=username).first()
        page_serializer = PageSerializer(pages).data
        user_serializer = UserSerializer(users).data

        response = Response()
        response.data = {
            "page": page_serializer,
            "user": user_serializer
        }
        return response
