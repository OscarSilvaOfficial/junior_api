from django.urls import path, include
from apps.posts.views import PostsViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('', PostsViewSet, basename="Posts")

urlpatterns = [
  path('', include(router.urls)),
]
