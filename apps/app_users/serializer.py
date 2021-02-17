from rest_framework import serializers
from django.contrib.auth.models import User
from apps.app_posts.models import Posts

class UsersSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = User
    fields= ['id', 'username', 'first_name', 'last_name', 'email']
    
class UserPostsSerializer(serializers.ModelSerializer):
  
  user_id = serializers.ReadOnlyField(source='user_id.username')
  
  class Meta:
    model = Posts
    fields = '__all__'
