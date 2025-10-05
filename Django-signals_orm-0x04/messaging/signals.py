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
