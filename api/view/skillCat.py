from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from portofolio.models.models import SkillCat
from api.serializers import SkillCatSerializer
from rest_framework.response import Response
from rest_framework import viewsets, authentication, permissions


class SkillCatViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows SkillCat to be viewed or edited.
    """
    queryset = SkillCat.objects.all()
    serializer_class = SkillCatSerializer


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def skillCatList(request):
    queryset = SkillCat.objects.all()
    serializer = SkillCatSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def skillCatDetail(request, pk):
    queryset = SkillCat.objects.get(id=pk)
    serializer = SkillCatSerializer(queryset, many=False)
    return Response(serializer.data)
