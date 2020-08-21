from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from portofolio.models.models import Education
from api.serializers import EducationSerializer
from rest_framework.response import Response
from rest_framework import viewsets, authentication, permissions

class EducationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows Education to be viewed or edited.
    """
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def educationList(request):
    queryset = Education.objects.all()
    serializer = EducationSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def educationDetail(request, pk):
    queryset = Education.objects.get(id=pk)
    serializer = EducationSerializer(queryset, many=False)
    return Response(serializer.data)
