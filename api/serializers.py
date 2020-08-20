from django.contrib.auth.models import User, Group
from rest_framework import serializers

from portofolio.models import LandingPage, SkillCat, Skill, Education, Experience, BlogCat, Blog, Gallery


class LandingPageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LandingPage


class SkillCatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SkillCat


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill


class EducationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Education


class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Experience


class BlogCatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogCat


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog


class GallerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gallery
