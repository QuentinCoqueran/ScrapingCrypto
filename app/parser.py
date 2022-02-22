from app.model.Coin import Coin
from app.model.Currency import Currency
from app.model.Report import Report


def parse_coin(coin_json):
    coin_instance = Coin(coin_json['id'], coin_json['name'], coin_json['symbol'], coin_json['market_cap_rank'])
    return coin_instance


def parse_vs_currencies(currency_string):
    currency_instance = Currency(currency_string)
    return currency_instance


def parse_reports(report_json):
    reports = []
    for report in report_json:
        coins = []
        currencies = []
        for coin_json in report['coins']:
            coins.append(parse_coin(coin_json))

        for curr_json in report['currencies']:
            currencies.append(parse_vs_currencies(curr_json))

        reports.append(Report(report['name'], coins, currencies))

    return reports
