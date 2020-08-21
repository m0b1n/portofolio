from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .view.blog import BlogViewSet, blogDetail, blogList
from .view.blogCat import blogCatList, BlogCatViewSet, blogCatDetail
from .view.education import EducationViewSet, educationDetail, educationList
from .view.experience import ExperienceViewSet, experienceDetail, experienceList
from .view.gallery import GalleryViewSet, galleryDetail, galleryList
from .view.landingPage import LandingPageViewSet, landingPageDetail, landingPageList
from .view.skill import SkillViewSet, skillDetail, skillList
from .view.skillCat import SkillCatViewSet, skillCatDetail, skillCatList


# Routers provide a way of automatically determining the URL conf.
from api import views
from api.views import UserViewSet
from api.views import apiOverview


router = routers.DefaultRouter()
router.register(r'landingpage', LandingPageViewSet)
router.register(r'skillcat', SkillCatViewSet)
router.register(r'skill', SkillViewSet)
router.register(r'education', EducationViewSet)
router.register(r'experience', ExperienceViewSet)
router.register(r'blogcat', BlogCatViewSet)
router.register(r'blog', BlogViewSet)
router.register(r'gallery', GalleryViewSet)
router.register(r'usersss', UserViewSet, basename='user')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', apiOverview, name="api-overview"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('userlogin', views.UserLogin.as_view(), name='user-login'),

    path('gallery-list/', galleryList, name="gallery-list"),
    path('gallery-detail/<str:pk>/', galleryDetail, name="gallery-detail"),

    path('blog-list/', blogList, name="blog-list"),
    path('blog-detail/<str:pk>/', blogDetail, name="blog-detail"),

    path('blogcat-list/', blogCatList, name="blogcat-list"),
    path('blogcat-detail/<str:pk>/', blogCatDetail, name="blogcat-detail"),

    path('education-list/', educationList, name="education-list"),
    path('education-detail/<str:pk>/', educationDetail, name="education-detail"),

    path('experience-list/', experienceList, name="experience-list"),
    path('experience-detail/<str:pk>/',
         experienceDetail, name="experience-detail"),

    path('landingpage-list/', landingPageList, name="landingpage-list"),
    path('landingpage-detail/<str:pk>/',
         landingPageDetail, name="landingpage-detail"),

    path('skill-list/', skillList, name="skill-list"),
    path('skill-detail/<str:pk>/', skillDetail, name="skill-detail"),

    path('skillcat-list/', skillCatList, name="skillcat-list"),
    path('skillcat-detail/<str:pk>/', skillCatDetail, name="skillcat-detail"),
]

urlpatterns += router.urls