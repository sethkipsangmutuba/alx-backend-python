# chats/views.py
from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer
from .permissions import IsOwner, IsParticipantOfConversation

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsParticipantOfConversation]  # Apply custom permission

    # Optional: ensure object-level permissions are enforced
    def get_permissions(self):
        permission_classes = [IsParticipantOfConversation]
        return [permission() for permission in permission_classes]
