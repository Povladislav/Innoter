from rest_framework.generics import GenericAPIView
from .permissions import IsUserAdm
from .models import User
# from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed


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
        return Response({"banned": f"successfully banned for {time} hours"})
