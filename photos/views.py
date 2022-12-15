from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from photos.models import Photo
from photos.serializers import PhotoCreateSerializer, PhotoReadOnlySerializer, PhotoReadOnlyRetriveSerializer

class PhotoViewSet(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoReadOnlySerializer

    def create(self, request, *args, **kwargs):
        serializer = PhotoCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PhotoReadOnlyRetriveSerializer(instance)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)