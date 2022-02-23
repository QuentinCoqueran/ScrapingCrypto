# coding: utf-8

import requests
import json

from app.model.Currency import Currency
from app.parser import parse_coin, parse_vs_currencies
import config


class RequestManager:

    def __init__(self):
        self.api_url = config.COIN_API_URL

    def get_currencies(self):
        """
        Return all the currencies available on the API
        """
        url = "{}simple/supported_vs_currencies".format(self.api_url)
        try:
            response = requests.get(url)
            currencies = []
            content = json.loads(response.content.decode('utf-8'))
            for currency in content:
                currencies.append(Currency(currency))
            return currencies
        except Exception as e:
            print(e)

    def search_coins(self, query):
        """
        Take the user entry, make an API call and return the search results
        """
        url = "{0}search?query={1}".format(self.api_url, query.lower())
        try:
            response = requests.get(url)
            content = json.loads(response.content.decode('utf-8'))
            coins = []
            for coin in content['coins'][0:5]:  # TODO: Vérifier si on peut subir un out of range
                coins.append(parse_coin(coin))
            return coins
        except Exception as e:
            print(e)


request_manager = RequestManager()
