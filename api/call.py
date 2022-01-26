# coding: utf-8

import requests
import json
class ApiCalls : 

    api_url = "https://api.coingecko.com/api/v3/"

    def __init__(self, API_URL) :


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

