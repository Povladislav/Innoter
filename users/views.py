from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import exceptions
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (DestroyModelMixin, ListModelMixin,
                                   RetrieveModelMixin, UpdateModelMixin)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin

from users.utils import generate_access_token, generate_refresh_token

from .models import User
from .serializers import UserSerializer


class user_view(ViewSetMixin, DestroyModelMixin,
                ListModelMixin, UpdateModelMixin,
                RetrieveModelMixin, GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class register_view(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class login_view(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    @method_decorator(ensure_csrf_cookie)
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        response = Response()
        user = User.objects.filter(email=email).first()
        if (user is None):
            raise exceptions.AuthenticationFailed('user not found')
        if (not user.check_password(password)):
            raise exceptions.AuthenticationFailed('wrong password')

        serialized_user = UserSerializer(user).data

        access_token = generate_access_token(user)
        refresh_token = generate_refresh_token(user)

        response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
        response.data = {
            'access_token': access_token,
            'user': serialized_user,
        }

        return response


class CurrentUserView(GenericAPIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class logout_view(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        response = Response()
        response.delete_cookie('csrftoken')
        response.data = {
            'message': 'success'
        }
        return response
