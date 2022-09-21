import datetime

from django.utils import timezone
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from blog.models import Page

from .models import User
from .permissions import IsUserAdm


class BanUsers(GenericAPIView):
    permission_classes = [IsUserAdm]

    def post(self, request, id):
        time = self.request.data['bantime']
        if time is None:
            user_to_ban = User.objects.get(pk=id)
            user_to_ban.is_active = False
            user_to_ban.is_blocked = True
            user_to_ban.save()
            return Response({"banned": "successfully permanently banned"})
        user_to_ban = User.objects.get(pk=id)
        user_to_ban.is_blocked = True
        user_to_ban.time_before_unban = timezone.now() + datetime.timedelta(minutes=time)
        user_to_ban.save()
        return Response({"banned": f"successfully banned for {time} minutes"})


class BanPages(GenericAPIView):
    permission_classes = [IsUserAdm]

    def post(self, request, id):
        time = self.request.data['bantime']
        page_to_ban = Page.objects.get(pk=id)
        page_to_ban.is_blocked = True
        page_to_ban.time_before_unban = timezone.now() + datetime.timedelta(minutes=time)
        page_to_ban.save()
        return Response({"banned": f"page successfully banned for {time} minutes"})
