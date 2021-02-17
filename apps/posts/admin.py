from django.contrib import admin
from .models import Posts

# Register your models here.

@admin.register(Posts)
class Posts(admin.ModelAdmin):
  list_display = ('user_id', 'title', 'content', 'date', 'tags')
  list_display_links = ('user_id',)
  search_fields = ('title',)
  list_per_page = 20