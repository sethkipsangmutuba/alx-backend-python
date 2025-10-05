from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def delete_user(request):
    user = request.user
    user.delete()
    messages.success(request, "Your account and all related data have been deleted.")
    return redirect('home')  # replace 'home' with your homepage URL name
