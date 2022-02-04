from model.Coin import Coin


def parse_coin(coin_json):
    coin_instance = Coin(coin_json['id'], coin_json['name'], coin_json['symbol'], coin_json['market_cap_rank'])
    return coin_instance
