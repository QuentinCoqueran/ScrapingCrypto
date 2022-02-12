# coding: utf-8

import requests
import json

from app.api.Parser import Parser


class RequestManager:

    def __init__(self, api_url):
        self.api_url = api_url

    @property
    def api_url(self):
        return self.__api_url

    @api_url.setter
    def api_url(self, api_url):
        self.__api_url = api_url

    def get_vs_currencies(self):
        """
        Return all the currencies available on the API
        """
        url = "{}simple/supported_vs_currencies".format(self.api_url)
        try:
            response = requests.get(url)
            content = json.loads(response.content.decode('utf-8'))
            return content
        except Exception:
            print("Requête invalide")

    def search_currencies(self, query):
        """
        Take the user entry, make an API call and return the search results
        """
        url = "{0}search?query={1}".format(self.api_url, query.lower())
        try:
            response = requests.get(url)
            content = json.loads(response.content.decode('utf-8'))
            coins = []
            for coin in content['coins'][0:5]:  # TODO: Vérifier si on peut subir un out of range
                coins.append(Parser.parse_coin(coin))
            return coins
        except Exception:
            print("Aucun résultat")
