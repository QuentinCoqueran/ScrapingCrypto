from app.model.Coin import Coin
from app.model.Currency import Currency


def parse_coin(coin_json):
    coin_instance = Coin(coin_json['id'], coin_json['name'], coin_json['symbol'], coin_json['market_cap_rank'])
    return coin_instance


def parse_vs_currencies(currency_string):
    currency_instance = Currency(currency_string)
    return currency_instance
