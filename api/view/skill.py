from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from portofolio.models.models import Skill
from api.serializers import SkillSerializer
from rest_framework.response import Response
from rest_framework import viewsets, authentication, permissions


class SkillViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows Skill to be viewed or edited.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def skillList(request):
    queryset = Skill.objects.all()
    serializer = SkillSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def skillDetail(request, pk):
    queryset = Skill.objects.get(id=pk)
    serializer = SkillSerializer(queryset, many=False)
    return Response(serializer.data)
