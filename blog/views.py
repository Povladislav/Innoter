from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Tag
from .serializers import TagSerializer


class CreateTag(GenericAPIView):
    # Using AllowAny while have not designed new permissions
    permission_classes = [AllowAny]
    serializer_class = TagSerializer

    def post(self, request):
        serializer = TagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(request.data)
