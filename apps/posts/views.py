from django.http import JsonResponse
from rest_framework import viewsets
from .models import Posts
from .serializer import PostSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class PostsViewSet(viewsets.ModelViewSet):
  """ Classe referente a todas as ações para posts """
  
  queryset = Posts.objects.all()
  serializer_class = PostSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]
