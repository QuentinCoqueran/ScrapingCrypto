# coding: utf-8

import requests
import json

from app.utils.parser import parse_coin
from app.model.Currency import Currency
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

    def get_coin_thumb_by_coin_id(self, coin_id):
        """
        Return the price by coin in a currency
        """
        url = "{}coins/{}".format(self.api_url, coin_id)
        try:
            response = requests.get(url)
            content = json.loads(response.content.decode('utf-8'))
            return content['image']['thumb']
        except Exception as e:
            print(e)

    def get_coin_data(self, currency, coins):

        url = "{}coins/markets?vs_currency={}&ids={}&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=24h".format(
            self.api_url, currency.short_name, coins)
        try:
            response = requests.get(url)
            content = json.loads(response.content.decode('utf-8'))
            content = {coin_data['id']: {'price': coin_data['current_price'],
                                         '24_change': coin_data['price_change_percentage_24h']} for coin_data in
                       content}
            return content
        except Exception as e:
            print(e)

    def get_coin_price_by_currencies(self, report):
        """
        Return the price by coin in a currency
        """
        coins = ",".join([coin.id for coin in report.coins])
        currencies = {currency.short_name: self.get_coin_data(currency, coins) for currency in report.currencies}
        return currencies


request_manager = RequestManager()
