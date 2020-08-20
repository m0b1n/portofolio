from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

# Routers provide a way of automatically determining the URL conf.
from api import views
from api.views import LandingPageViewSet, SkillCatViewSet, SkillViewSet, EducationViewSet, ExperienceViewSet, BlogCatViewSet, BlogViewSet, GalleryViewSet, ListUsers

router = routers.DefaultRouter()
router.register(r'landingpage', LandingPageViewSet)
router.register(r'skillcat', SkillCatViewSet)
router.register(r'skill', SkillViewSet)
router.register(r'education', EducationViewSet)
router.register(r'experience', ExperienceViewSet)
router.register(r'blogcat', BlogCatViewSet)
router.register(r'blog', BlogViewSet)
router.register(r'gallery', GalleryViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('user/', views.ListUsers.as_view(), name='user'),
    path('users/', views.hello_world, name='users'),
    path('l/', views.SnippetList.as_view(), name='l')
]
