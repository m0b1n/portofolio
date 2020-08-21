from rest_framework.decorators import api_view, authentication_classes, permission_classes
from portofolio.models.models import BlogCat
from rest_framework.permissions import IsAuthenticated
from api.serializers import BlogCatSerializer
from rest_framework.response import Response
from rest_framework import viewsets, authentication, permissions

class BlogCatViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows BlogCat to be viewed or edited.
    """
    queryset = BlogCat.objects.all()
    serializer_class = BlogCatSerializer


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def blogCatList(request):
    queryset = BlogCat.objects.all()
    serializer = BlogCatSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def blogCatDetail(request, pk):
    queryset = BlogCat.objects.get(id=pk)
    serializer = BlogCatSerializer(queryset, many=False)
    return Response(serializer.data)
