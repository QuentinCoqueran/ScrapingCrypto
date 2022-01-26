from model.Coin import Coin

def parse_coin(coin_dict):
    coins = []
    for coin in coin_dict:
        coin_instance = Coin(coin['id'],coin['name'],coin['symbol'],coin['market_cap_rank'])
        print(coin_instance.name)