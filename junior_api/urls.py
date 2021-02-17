from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', admin.site.urls),
    path('posts/', include('apps.app_posts.urls')),
    path('users/', include('apps.app_users.urls')),
]