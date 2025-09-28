from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Message

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'content', 'created_at']
