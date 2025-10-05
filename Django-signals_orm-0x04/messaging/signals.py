from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory

# Task 0: Notification on new message
@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.receiver,
            message=instance
        )

# Task 1: Log message edits
@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:  # only if message already exists
        previous = Message.objects.get(pk=instance.pk)
        if previous.content != instance.content:
            # Save old content to MessageHistory
            MessageHistory.objects.create(
                message=instance,
                old_content=previous.content
            )
            instance.edited = True  # mark as edited


from django.db.models.signals import post_delete
from django.contrib.auth.models import User
from .models import Message, Notification, MessageHistory

@receiver(post_delete, sender=User)
def delete_user_related_data(sender, instance, **kwargs):
    # Delete messages sent or received by the user
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()
    
    # Delete notifications linked to the user
    Notification.objects.filter(user=instance).delete()
    
    # Delete message history linked to deleted messages
    MessageHistory.objects.filter(message__sender=instance).delete()
    MessageHistory.objects.filter(message__receiver=instance).delete()

