from rest_framework.permissions import IsAuthenticated
from api.serializers import BlogSerializer
from portofolio.models.models import Blog
from rest_framework.response import Response
from rest_framework import viewsets, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes


class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows Blog to be viewed or edited.
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def blogList(request):
    blog = Blog.objects.all()
    serializer = BlogSerializer(blog, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def blogDetail(request, pk):
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data)
