from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import LandingPageSerializer, SkillCatSerializer, SkillSerializer, EducationSerializer, ExperienceSerializer, BlogCatSerializer, BlogSerializer, GallerySerializer
from portofolio.models.models import LandingPage, SkillCat, Skill, Education, Experience, BlogCat, Blog, Gallery


class LandingPageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows LandingPage to be viewed or edited.
    """
    queryset = LandingPage.objects.all().order_by('-create_date')
    serializer_class = LandingPageSerializer   


class SkillCatViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows SkillCat to be viewed or edited.
    """
    queryset = SkillCat.objects.all()
    serializer_class = SkillCatSerializer


class SkillViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows Skill to be viewed or edited.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class EducationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows Education to be viewed or edited.
    """
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class ExperienceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows Experience to be viewed or edited.
    """
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class BlogCatViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows BlogCat to be viewed or edited.
    """
    queryset = BlogCat.objects.all()
    serializer_class = BlogCatSerializer

class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows Blog to be viewed or edited.
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class GalleryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows Gallery to be viewed or edited.
    """
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
