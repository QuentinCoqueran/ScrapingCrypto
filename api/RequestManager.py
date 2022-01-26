# coding: utf-8

import requests
import json

class RequestManager : 

    api_url = ""

    def __init__(self, _api_url) :
        self.api_url = _api_url

    def get_vs_currencies(self) :
        """
        Recupère les devises de comparaison
        
        Appel API retourne la liste des devises
        """

        url = "{}simple/supported_vs_currencies".format(self.api_url)
        try :
            response = requests.get(url)
            content = json.loads(response.content.decode('utf-8'))
            return content
        except requests.exceptions.RequestException :
            raise
    
    def search_currencies(self, user_input) :
        """
        Recupère l'entrée de l'utilisateur et retourne les informations de la recherche
        
        Appel API retourne les infos de la recherche de l'utilisateur
        """

        url = "{}search?query=".format(self.api_url)
        try :
            response = requests.get(url + user_input)
            content = json.loads(response.content.decode('utf-8'))
            return content['coins'][0:3]
        except requests.exceptions.RequestException :
            raise

