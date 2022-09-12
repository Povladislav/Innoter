import os

import jwt
from rest_framework.exceptions import AuthenticationFailed

from .models import User

secret_key = os.environ.get("secret_key")
class JWTAuthenticationMiddleware:
    def __init__(self, response):
        self.get_response = response

    def __call__(self, request):
        response = self.get_response(request)
        jwt_token = request.headers.get('authorization', None)
        if not jwt_token:
            return response
        try:
            payload = jwt.decode(jwt_token,secret_key, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(id=payload['id']).first()
        request.user = user
        return response