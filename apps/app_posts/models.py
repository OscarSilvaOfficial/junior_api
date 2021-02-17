from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  content = models.TextField()
  date = models.DateField()
  tags = models.CharField(max_length=100)
  
  def __str__(self):
      return self.user_id.username
    
  class Meta:
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'