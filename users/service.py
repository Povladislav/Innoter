import datetime

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import User
from .permissions import IsUserAdm

from django.utils import timezone


class AdminLogic(GenericAPIView):
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
