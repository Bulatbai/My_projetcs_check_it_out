
from django.shortcuts import render


def homepage(request):
 
    return render(request, 'home.html')
# Create your views here.

def pirofile(request):
    user = request.user
    profile_object = user.profile
    return render(request, 'profiles.html', {'profile': profile_object})