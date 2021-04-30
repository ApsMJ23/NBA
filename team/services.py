import os
import requests
from django.http import HttpRequest



def get_players():
    url = "https://nba-players.herokuapp.com/players-stats/"
    response = requests.request("GET", url)
    data = response.json()
    return data


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


#get_meta()