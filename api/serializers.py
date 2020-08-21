from django.contrib.auth.models import User, Group
from rest_framework import serializers

from portofolio.models.models import LandingPage, SkillCat, Skill, Education, Experience, BlogCat, Blog, Gallery
from portofolio.models.user import MyUser
from .models import ResponseMessage


class ResponseMessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=200)
    content = serializers.SerializerMethodField()
    created = serializers.DateTimeField()
    exception = serializers.StringRelatedField()
    status = serializers.CharField(max_length=200)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'


class LandingPageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LandingPage
        fields = '__all__'


class SkillCatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SkillCat
        fields = '__all__'


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class EducationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


class BlogCatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogCat
        fields = '__all__'


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class GallerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'
