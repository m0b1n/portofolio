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
from api.serializers import MyUserSerializer, SignUpMyUserSerializer
from portofolio.models.models import LandingPage, SkillCat, Skill, Education, Experience, BlogCat, Blog, Gallery
from portofolio.models.user import MyUser

from .models import ResponseMessage
from pytz import unicode
from rest_framework.generics import get_object_or_404
import logging

from django.contrib.auth import authenticate, login, logout

logger = logging.getLogger('django.server')


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


class UserSignUp(APIView):
    """
    A view that sign up the given cred
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        logger.info(request.data)
        serializer = SignUpMyUserSerializer(data=request.data)

        if serializer.is_valid():
            MyUser.objects.create_user(
                serializer.data['phone_number'],
                serializer.data['date_of_birth'],
                serializer.data['password']
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    """
    A view that login the given cred
    """

    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):

        logger.info(request.data)
        serializer = MyUserSerializer(data=request.data)

        if serializer.is_valid():
            user = authenticate(
                phone_number=serializer.data['username'], password=serializer.data['password'])
            if user is not None:
                # A backend authenticated the credentials
                comment = ResponseMessage(
                    message='مشخصات کاربر', exception=Exception('User Found'), status=status.HTTP_200_OK, content=UserSerializer(user).data)
                msgserializer = ResponseMessageSerializer(comment)
                login(request, user)
                return Response(msgserializer.data)
            else:
                # No backend authenticated the credentials
                logger.info('user is None')
                logout(request)
                comment = ResponseMessage(
                    message='یوزری با این مشخصات پیدا نشد', exception=Exception('No User Found'), status=status.HTTP_404_NOT_FOUND, content=request.data)
                msgserializer = ResponseMessageSerializer(comment)
                return Response(msgserializer._errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data)

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
