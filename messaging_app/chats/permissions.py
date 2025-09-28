from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of a message to view/edit it.
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


# chats/permissions.py
from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """Allows access only to owners of the object"""
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsParticipantOfConversation(permissions.BasePermission):
    """
    Allows access only to participants of a conversation.
    Assumes Message has a foreign key to Conversation with a 'participants' field.
    """
    def has_object_permission(self, request, view, obj):
        # Check if the user is in the participants list of the conversation
        return request.user in obj.conversation.participants.all()
