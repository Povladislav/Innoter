import datetime
import os

import jwt
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer

secret_key = os.environ.get("secret_key")


class RegisterView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("User not found!")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")

        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
            "iat": datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, secret_key, algorithm='HS256')

        response = Response()
        request.META["HTTP_AUTHORIZATION"] = token
        response.set_cookie(key="jwt", value=token, httponly=True)
        response.data = {
            "jwt": token
        }

        return response


class LogoutView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(method='post', request_body=UserSerializer)
    @api_view(['POST'])
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }

        return response
