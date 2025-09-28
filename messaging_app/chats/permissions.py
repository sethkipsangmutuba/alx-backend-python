from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of a message to view/edit it.
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
