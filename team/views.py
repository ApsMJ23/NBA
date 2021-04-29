from django.shortcuts import render
from users import views
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import services

# Create your views here.
teams = services.get_teams()

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    else:
        return render(request, "team/index.html",{
            "teams": teams
        })