# coding: utf-8

from app.api.request_manager import RequestManager
from app.App import App
from app.model.Coin import Coin
from app.model.Currency import Currency
from app.model.Report import Report


def main():
    app = App()
    app.start()


if __name__ == '__main__':
    main()

# coin = Coin("bitcoin", "Bitcoin", "BTC", 1)
# coin2 = Coin("ethereum", "Ethereum", "Ether", 1)
# currency = Currency("eur")
# currency2 = Currency("usd")
#
# coins = [coin, coin2]
# currencies = [currency, currency2]
# report = Report("mon rapport", coins, currencies)
# print(report)