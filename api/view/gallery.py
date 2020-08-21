from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import permissions
from portofolio.models.models import Gallery
from api.serializers import GallerySerializer
from rest_framework import viewsets, authentication, permissions


class GalleryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Gallery to be viewed or edited.
    """

    permission_classes = [permissions.IsAuthenticated]

    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def galleryList(request):
    gallery = Gallery.objects.all()
    serializer = GallerySerializer(gallery, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def galleryDetail(request, pk):
    gallery = Gallery.objects.get(id=pk)
    serializer = GallerySerializer(gallery, many=False)
    return Response(serializer.data)
