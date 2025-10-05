from django.db import models

class UnreadMessagesManager(models.Manager):
    def unread_for_user(self, user):
        """
        Returns unread messages for a given user.
        Optimized to fetch only required fields.
        """
        return self.filter(receiver=user, read=False).only('id', 'sender', 'receiver', 'content', 'timestamp')
