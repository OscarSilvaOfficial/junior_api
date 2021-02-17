from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from apps.posts.models import Posts
from rest_framework import status
from rest_framework.response import Response
from observers.functions import create_email
from .serializer import UsersSerializer, UserPostsSerializer
from rest_framework.mixins import CreateModelMixin as create_mixin, UpdateModelMixin as update_mixin


class UsersViewSet(viewsets.ModelViewSet):
    """ Classe referente a todas as ações para os usuários """

    queryset = User.objects.all()
    serializer_class = UsersSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def update(self, request, *args, **kwargs):
      response = update_mixin.update(self, request, *args, **kwargs)
      create_email(
        request.data, 
        'Opa, seu cadastro foi atualizado',
        'estamos aqui para informar que seu usuario foi atualizado'
      )
      return Response(response, status=status.HTTP_201_CREATED)

    def create(self, request, *args, **kwargs):
      response = create_mixin.create(self, request, *args, **kwargs)
      create_email(
        request.data, 
        'Seja muito bem vindo',
        'estamos muito felizes de estar com voce'
      )
      return Response(response, status=status.HTTP_201_CREATED)


class UserPosts(generics.ListAPIView):
    """ Listagem de Posts de um usuário """

    serializer_class = UserPostsSerializer
    
    def get_queryset(self):
        return Posts.objects.filter(user_id=self.kwargs['pk'])
