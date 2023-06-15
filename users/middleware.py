import os

import jwt
from rest_framework.exceptions import AuthenticationFailed

from .models import User

secret_key = os.environ.get("secret_key")


class JWTAuthenticationMiddleware:
    def __init__(self, response):
        self.get_response = response

    def __call__(self, request):
        exclude_path = ("/accounts/login/", "/accounts/register/")
        jwt_token = request.headers.get('Authorization')
        if not jwt_token or request.path in exclude_path:
            return self.get_response(request)
        access_token = jwt_token.split(" ")[1]

        try:
            payload = jwt.decode(access_token, secret_key, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(id=payload['user_id']).first()
        request.user = user
        response = self.get_response(request)
        return response
