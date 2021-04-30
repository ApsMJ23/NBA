from django.shortcuts import render
from users import views
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import services

# Create your views here.
players = services.get_players()
teams = services.get_teams()
def index(request): 

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    else:
        return render(request, "team/index.html",{
            "teams": teams,
            "b" : "Nets"
        })


def player(request,tm_abb):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    else:
        p = []
        first = []
        last = []
        c = 0
        for player in players:
            if player['team_acronym'].lower() == tm_abb.lower():
                p.append(player)
        for pl in p:
            a= p[c]['name']
            a.split()
            first.append(a.split()[0])
            last.append(a.split()[1])
            c+=1
        mylist = zip(p,last,first)
        return render(request, "team/player.html",{
                    "player" : mylist,
                    "dlo" : r"D'Angelo",
                    "nan" : r"Nance"
                })

