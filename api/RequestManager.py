# coding: utf-8

import requests
import json
import api.custom_parser

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
        except Exception :
            print("Mauvaise requete")
    
    def search_currencies(self, query) :
        """
        Recupère l'entrée de l'utilisateur et retourne les informations de la recherche
        
        Appel API retourne les infos de la recherche de l'utilisateur
        """

        url = "{0}search?query={1}".format(self.api_url, query.lower())
        try :
            response = requests.get(url)
            content = json.loads(response.content.decode('utf-8'))
            return api.custom_parser.parse_coin(content['coins'][0:3])
        except Exception :
            print("Aucun resultat")

