from django.urls import path, include
from .views import UsersViewSet, UserPosts
from rest_framework import routers


router = routers.DefaultRouter()
router.register('', UsersViewSet, basename="Users")

urlpatterns = [
  path('', include(router.urls)),
  path('<int:pk>/posts/', UserPosts.as_view()),
]
