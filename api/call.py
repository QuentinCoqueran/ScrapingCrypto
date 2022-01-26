# coding: utf-8

import requests
import json


API_URL = "https://api.coingecko.com/api/v3/"

def get_vs_currencies() :
    """
    Recupère les devises de comparaison
    
    Appel API retourne la liste des devises
    """

    url = "{}simple/supported_vs_currencies".format(API_URL)
    try :
        response = requests.get(url)
        content = json.loads(response.content.decode('utf-8'))
        return content
    except requests.exceptions.RequestException :
        raise

