from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('chats.auth')),  # JWT endpoints
    path('api/chats/', include('chats.urls')),  # your chat endpoints
]
