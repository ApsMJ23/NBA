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
        'x-rapidapi-key': "a7a397fd89msh4c17f53b3218f40p1bd67cjsn97378b49e88a",
        'x-rapidapi-host': "free-nba.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    data_list = []
    for i in range(len(data['data'])):
         data_list.append(data['data'][i])
         
    return data_list