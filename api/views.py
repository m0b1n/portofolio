from django.contrib.auth.models import User, Group
from rest_framework import viewsets, authentication, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from api.serializers import LandingPageSerializer, SkillCatSerializer, SkillSerializer, EducationSerializer, ExperienceSerializer, BlogCatSerializer, BlogSerializer, GallerySerializer
from portofolio.models.models import LandingPage, SkillCat, Skill, Education, Experience, BlogCat, Blog, Gallery
from portofolio.models.user import MyUser


class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, format=None):
        snippets = Education.objects.all()
        serializer = EducationSerializer(snippets, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = EducationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.phone_number for user in MyUser.objects.all()]
        return Response(usernames)

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
