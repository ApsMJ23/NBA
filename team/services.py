import os
import requests
from django.http import HttpRequest

def get_players():
    url = "https://free-nba.p.rapidapi.com/players"

    querystring = {"page":"0","per_page":"50"}

    headers = {
        'x-rapidapi-key': os.getenv('DO_ACCESS_TOKEN'),
        'x-rapidapi-host': "free-nba.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()
    data_list = []
    for i in range(len(data['data'])):
         data_list.append(data['data'][i])


def get_teams():
    url = "https://free-nba.p.rapidapi.com/teams"

    querystring = {"page":"0"}

    headers = { 
        'x-rapidapi-key': os.getenv('DO_ACCESS_TOKEN'),
        'x-rapidapi-host': "free-nba.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    data_list = []
    for i in range(len(data['data'])):
         data_list.append(data['data'][i])
         
    return data_list