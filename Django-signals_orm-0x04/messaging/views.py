from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from .models import Message

# Task 2: Delete user and related data
@login_required
def delete_user(request):
    user = request.user
    user.delete()
    messages.success(request, "Your account and all related data have been deleted.")
    return redirect('home')  # replace 'home' with your homepage URL name

# Task 3: Threaded messages for logged-in user
@login_required
def user_threaded_messages(request):
    """
    Retrieves all top-level messages for the logged-in user with replies,
    optimized using select_related and prefetch_related.
    """
    top_messages = Message.objects.filter(receiver=request.user, parent_message__isnull=True) \
        .select_related('sender', 'receiver') \
        .prefetch_related(
            Prefetch('replies', queryset=Message.objects.select_related('sender', 'receiver'))
        ).order_by('-timestamp')

    # Recursive function to flatten threads
    def get_full_thread(msg):
        thread = [msg]
        for reply in msg.replies.all():
            thread.extend(get_full_thread(reply))
        return thread

    all_threads = []
    for msg in top_messages:
        all_threads.append(get_full_thread(msg))

    return render(request, 'messaging/threaded_messages.html', {'threads': all_threads})
