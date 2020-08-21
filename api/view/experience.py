from rest_framework.permissions import IsAuthenticated
from portofolio.models.models import Experience
from api.serializers import ExperienceSerializer
from rest_framework.response import Response
from rest_framework import viewsets, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes


class ExperienceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows Experience to be viewed or edited.
    """
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def experienceList(request):
    queryset = Experience.objects.all()
    serializer = ExperienceSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def experienceDetail(request, pk):
    queryset = Experience.objects.get(id=pk)
    serializer = ExperienceSerializer(queryset, many=False)
    return Response(serializer.data)
