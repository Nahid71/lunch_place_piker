from django.shortcuts import redirect
from django.conf import settings 


# Create your views here.

def admin_logout(request):
    return redirect(settings.LOGOUT_URL)