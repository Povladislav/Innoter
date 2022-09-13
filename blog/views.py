from rest_framework import status
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


class ReadTag(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = TagSerializer

    def get(self, request):
        if request.query_params:
            tags = Tag.objects.filter(**request.query_params.dict())
            serializer = TagSerializer(tags, many=True)
        else:
            tags = Tag.objects.all()
            serializer = TagSerializer(tags, many=True)
        if tags:
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UpdateTag(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = TagSerializer

    def put(self, request, pk):
        tag = Tag.objects.get(pk=pk)
        data = TagSerializer(instance=tag, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
