from django.http import JsonResponse
from rest_framework import viewsets
from .models import Posts
from .serializer import PostSerializer

class PostsViewSet(viewsets.ModelViewSet):
  """ Classe referente a todas as ações para posts """
  
  queryset = Posts.objects.all()
  serializer_class = PostSerializer
