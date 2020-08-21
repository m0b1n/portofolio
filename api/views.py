from django.contrib.auth.models import User, Group
from rest_framework import viewsets, authentication, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import action

from api.serializers import LandingPageSerializer, SkillCatSerializer, SkillSerializer, EducationSerializer, ExperienceSerializer, BlogCatSerializer, BlogSerializer, GallerySerializer, UserSerializer, ResponseMessageSerializer
from portofolio.models.models import LandingPage, SkillCat, Skill, Education, Experience, BlogCat, Blog, Gallery
from portofolio.models.user import MyUser

from .models import ResponseMessage
from pytz import unicode
from rest_framework.generics import get_object_or_404


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def apiOverview(request):
    api_urls = {
        'Gallery': {
            1: 'GalleryModelViewSet',
            2: '/gallery-list/',
            3: '/gallery-detail/'},
        'Blog': {
            1: 'BlogModelViewSet',
            2: '/blog-list/',
            3: '/blog-detail/'},
        'BlogCat': {
            1: 'BlogCatModelViewSet',
            2: '/blogcat-list/',
            3: '/blogcat-detail/'},
        'Education': {
            1: 'EducationModelViewSet',
            2: '/education-list/',
            3: '/education-detail/'},
        'Experience': {
            1: 'ExperienceModelViewSet',
            2: '/experience-list/',
            3: '/experience-detail/'},
        'LandingPage': {
            1: 'LandingPageModelViewSet',
            2: '/landingpage-list/',
            3: '/landingpage-detail/'},
        'Skill': {
            1: 'SkillModelViewSet',
            2: '/skill-list/',
            3: '/skill-detail/'},
        'SkillCat': {
            1: 'SkillCatModelViewSet',
            2: '/skillcat-list/',
            3: '/skillcat-detail/'},
    }

    return Response(api_urls)


class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = MyUser.objects.all()
        serializer = UserSerializer(queryset, many=True)
        res = ResponseMessage(message="asd", exception=Exception(
            "exception1"), content=queryset, status=status.HTTP_200_OK, created=None)
        ser = ResponseMessageSerializer(res)
        return Response(ser.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserCountView(APIView):
    """
    A view that returns the count of active users in JSON.
    """
    renderer_classes = [JSONRenderer]
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        user_count = MyUser.objects.all()
        serializer = UserSerializer(
            user_count, many=True, context={'request': request})
        content = {'user_count': serializer}
        return Response(content)


class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        snippets = Education.objects.all()
        serializer = EducationSerializer(
            snippets, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = EducationSerializer(
            data=request.data, context={'request': request})
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


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'user': unicode(request.user),  # `django.contrib.auth.User` instance.
        'auth': unicode(request.auth),  # None
    }
    return Response(content)
