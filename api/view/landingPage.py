from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from portofolio.models.models import LandingPage
from api.serializers import LandingPageSerializer
from rest_framework.response import Response
from rest_framework import viewsets, authentication, permissions


class LandingPageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows LandingPage to be viewed or edited.
    """
    queryset = LandingPage.objects.all().order_by('-create_date')
    serializer_class = LandingPageSerializer


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def landingPageList(request):
    queryset = LandingPage.objects.all()
    serializer = LandingPageSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def landingPageDetail(request, pk):
    queryset = LandingPage.objects.get(id=pk)
    serializer = LandingPageSerializer(queryset, many=False)
    return Response(serializer.data)
