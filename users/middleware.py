import json
import jwt
import logging
from django.http import HttpResponse
from .models import User
from rest_framework.exceptions import AuthenticationFailed


class JWTAuthenticationMiddleware:
    def __init__(self, response):
        self.get_response = response

    def __call__(self, request):
        response = self.get_response(request)
        jwt_token = request.headers.get('authorization', None)
        if not jwt_token:
            return response
        try:
            payload = jwt.decode(jwt_token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(id=payload['id']).first()
        request.user = user
        return response