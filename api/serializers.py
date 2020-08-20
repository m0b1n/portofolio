from django.contrib.auth.models import User, Group
from rest_framework import serializers

from portofolio.models.models import LandingPage, SkillCat, Skill, Education, Experience, BlogCat, Blog, Gallery


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
